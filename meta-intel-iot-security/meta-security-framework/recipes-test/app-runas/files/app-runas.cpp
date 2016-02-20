// (C) Copyright 2015 Intel Corporation
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.

#include <security-manager.h>

#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

#include <sys/types.h>
#include <sys/wait.h>

#include <string>
#include <vector>

#define CHECK(x) { \
        int _ret = x; \
        if (_ret != SECURITY_MANAGER_SUCCESS) { \
            fprintf(stderr, "Failure in %s:%d: %s: %d = %s\n", __FILE__, __LINE__, #x, _ret, security_manager_strerror((lib_retcode)_ret)); \
            return EXIT_FAILURE; \
        } \
   }

static int do_install(app_inst_req *preq)
{
    CHECK(security_manager_app_install(preq));
    return 0;
}

static int do_uninstall(app_inst_req *preq)
{
    CHECK(security_manager_app_uninstall(preq));
    return 0;
}

static int do_run(const char *appid, const char *uid, const char *file, char *const argv[])
{
    if (!appid || !uid) {
        fprintf(stderr, "Always need appid, uid for app startup.\n");
        return EXIT_FAILURE;
    }

    pid_t child = fork();
    if (child == -1) {
        perror("fork");
        return EXIT_FAILURE;
    } else if (child) {
        int status;
        child = waitpid(child, &status, 0);
        if (child == -1) {
            perror("waitpid");
            return EXIT_FAILURE;
        }
    } else {
        // We cannot change the UID before security_manager_prepare_app()
        // (because then setup_smack() fails to change Smack labels of
        // our fds) and we cannot change the UID after it (because then
        // security_manager_drop_process_privileges() has already dropped
        // the necessary CAP_SETUID.
        // Instead, we need to do the steps from security_manager_prepare_app()
        // ourselves.
        CHECK(security_manager_set_process_label_from_appid(appid));
        CHECK(security_manager_set_process_groups_from_appid(appid));
        if (setuid(atoi(uid))) {
            fprintf(stderr, "setuid(%s): %s\n", uid, strerror(errno));
            exit(EXIT_FAILURE);
        }
        CHECK(security_manager_drop_process_privileges());
        // CHECK(security_manager_prepare_app(appid));

        execvp(file, argv);
        fprintf(stderr, "execvp(%s): %s", argv[optind], strerror(errno));
        exit(EXIT_FAILURE);
    }
    return 0;
}

int main(int argc, char **argv)
{
    int flags, opt;
    int nsecs, tfnd;
    const char *appid = NULL;
    const char *pkgid = NULL;
    const char *uid = NULL;
    std::vector<const char *> privileges;
    std::vector< std::pair<app_install_path_type, std::string> > paths;
    int install = 0, uninstall = 0, run = 0;

    while ((opt = getopt(argc, argv, "a:p:u:r:t:ide")) != -1) {
        switch (opt) {
        case 'a':
            appid = optarg;
            break;
        case 'p':
            pkgid = optarg;
            break;
        case 'u':
            uid = optarg;
            break;
        case 'r':
            privileges.push_back(optarg);
            break;
        case 't': {
            const char *colon = strchr(optarg, ':');
            if (!colon) {
                fprintf(stderr, "-t parameter must be of the format <type>:<path>");
                return EXIT_FAILURE;
            }
            std::string typestr(optarg, colon - optarg);
            std::string path(colon + 1);
            app_install_path_type type;
            if (typestr == "private") {
                type = SECURITY_MANAGER_PATH_PRIVATE;
            } else if (typestr == "public") {
                type = SECURITY_MANAGER_PATH_PUBLIC;
            } else if (typestr == "public-ro") {
                type = SECURITY_MANAGER_PATH_PUBLIC_RO;
            } else if (typestr == "rw") {
                type = SECURITY_MANAGER_PATH_RW;
            } else if (typestr == "ro") {
                type = SECURITY_MANAGER_PATH_PRIVATE;
            } else {
                fprintf(stderr, "Invalid -t type: %s", typestr.c_str());
                return EXIT_FAILURE;
            }
            paths.push_back(std::make_pair(type, path));
            break;
        }
        case 'i':
            install = 1;
            break;
        case 'd':
            uninstall = 1;
            break;
        case 'e':
            run = 1;
            break;
        default: /* '?' */
            fprintf(stderr,
                    "Usage: %s -i|-e|-d -a appid -u uid -p pkgid -r privilege1 ... -t private|public|public-ro|rw:<path> ... -- command args\n"
                    "       -i = install, command ignored\n"
                    "       -e = run command, privileges and pkgid ignored\n"
                    "       -d = uninstall, command and privileges ignored\n"
                    "       Install, run, and uninstall can be combined into a single invocation.\n",
                    argv[0]);
            exit(EXIT_FAILURE);
            break;
        }
    }

    if ((install || uninstall) &&
        (!appid || !pkgid || !uid)) {
         fprintf(stderr, "Always need appid, pkgid, uid for app install or uninstall.\n");
         return EXIT_FAILURE;
    }
    if (run && optind >= argc) {
        fprintf(stderr, "Expected command after options\n");
        return EXIT_FAILURE;
    }

    app_inst_req *preq;
    CHECK(security_manager_app_inst_req_new(&preq));
    if (appid) {
        CHECK(security_manager_app_inst_req_set_app_id(preq, appid));
    }
    if (pkgid) {
        CHECK(security_manager_app_inst_req_set_pkg_id(preq, pkgid));
    }
    if (uid) {
        CHECK(security_manager_app_inst_req_set_uid(preq, atoi(uid)));
    }
    for (size_t i = 0; i < paths.size(); i++) {
        security_manager_app_inst_req_add_path(preq, paths[i].second.c_str(), paths[i].first);
    }
    for (size_t i = 0; i < privileges.size(); i++) {
        CHECK(security_manager_app_inst_req_add_privilege(preq, privileges[i]));
    }

    int result = 0;
    bool install_failed = false;
    if (install) {
        result = do_install(preq);
        if (result) {
            install_failed = true;
        }
    }
    if (run && !install_failed) {
        int run_result = do_run(appid, uid, argv[optind], argv + optind);
        if (run_result) {
            result = run_result;
        }
    }
    if (uninstall && !install_failed) {
        int uninstall_result = do_uninstall(preq);
        if (uninstall_result) {
            result = uninstall_result;
        }
    }

    security_manager_app_inst_req_free(preq);
    return result;
}
