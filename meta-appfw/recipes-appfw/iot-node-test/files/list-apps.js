/*
 * Copyright (c) 2015, Intel Corporation
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are
 * met:
 *
 *   * Redistributions of source code must retain the above copyright notice,
 *     this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *   * Neither the name of Intel Corporation nor the names of its contributors
 *     may be used to endorse or promote products derived from this software
 *     without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */


/////////////////////////
// parse command line
//
function parse_cmdline(app, argv) {
    var i, opt, optarg, d, libdir;

    i = 2;
    d = [];
    libdir = "";
    while (i < argv.length) {
        optstr = argv[i];
        optarg = argv[i + 1];
        
        switch (optstr) {
        case "--all":
        case "-a":
            app.which = "all";
            i++;
            break;

        case "--running":
        case "-r":
            app.which = "running";
            i++;
            break;

        case "--debug":
        case "-d":
            d[d.length] = optarg;
            i += 2;
            break;

        case "--libdir":
        case "-L":
            libdir = optarg;
            i += 2;
            break;

        default:
            console.log("Invalid/unknown option '" + optstr + "'");
            process.exit(0);
        }
    }

    app.iot = require(libdir ? libdir + "/iot-appfw.node" : "iot-appfw.node");
    app.iot.SetDebug(d);
}


var App = function () {
    this.iot = null;
    this.which = "all";
};


function ListCB (id, status, msg, apps) {
    console.log("Got reply for app list request " + id + "(" + status +
                ":" + msg + ")");

    if (status == 0) {
        console.log("Got a list of " + apps.length + " applications");
        for (var i in apps) {
            console.log("  " + apps[i].appid);
        }
    }

    process.exit(status);
}



/////////////////////////
// main script


var app = new App();

parse_cmdline(app, process.argv);


if (app.which == "running")
    req = app.iot.ListRunningApplications(ListCB);
else
    req = app.iot.ListAllApplications(ListCB);

if (!req) {
    console.log("Failed to query " + app.which + " applications.");
    process.exit(1);
}
else
    console.log("Got request id " + req);
    


