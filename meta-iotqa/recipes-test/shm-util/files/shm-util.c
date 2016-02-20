#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include <errno.h>
#include <sys/shm.h>

#define CREATE 1
#define REMOVE 2


static void __attribute__ ((__noreturn__)) usage(FILE * out)
{

	fprintf(out, "Helper tool to create/remove shared memory segments.\n");

	fprintf(out, "Options:\n");
	fprintf(out, " -m, --shmem <size>       create shared memory segment of size <size>\n");
	fprintf(out, " -r, --remove <shmid>        remove shared memory segment with id <shmid>\n");
    fprintf(out, " -p, --perm <permission>    permissions for memory segment to create. Default: 0644\n");

	fprintf(out, " -h, --help     display this help and exit\n");

	exit(out == stderr ? EXIT_FAILURE : EXIT_SUCCESS);
}

int main(int argc, char *argv[])
{
	int type, size, id, opt, ret;
	int permission = 0644;

	static const struct option longopts[] = {
		{"shmem", required_argument, NULL, 'm'},
		{"remove", required_argument, NULL, 'r'},
        {"perm", required_argument, NULL, 'p'},
		{"help", no_argument, NULL, 'h'},
		{NULL, 0, NULL, 0}
	};

	while((opt = getopt_long(argc, argv, "hm:r:p:", longopts, NULL)) != -1) {
		switch(opt) {
		case 'm':
			type=CREATE;
			size=atoi(optarg);
			break;
		case 'r':
			type=REMOVE;
			id=atoi(optarg);
            break;
        case 'p':
            permission = atoi(optarg);
            printf("Permission is: %d\n", permission);
			break;
		case 'h':
			usage(stdout);
			break;
		default:
			usage(stdout);
			return 1;
		}
	}

	if(type == CREATE) {
		key_t key;
		FILE *fp = fopen("/dev/urandom", "r");
		fread(&key, 1, sizeof(key), fp);
		fclose(fp);
		id = shmget(key, size, permission | IPC_CREAT);
		if(id != -1)
			printf("Shared memory id: %d\n", id);
		else {
			printf("Could not create memory with size %d\n", size);
			return EXIT_FAILURE;
		}	

	}
	else if(type == REMOVE) {
		ret = shmctl(id, IPC_RMID, NULL);
		if(ret < 0) {
			switch(errno) {
			case EACCES:
			case EPERM:
				printf("Permission denied for id %d\n", id);
				break;
			case EINVAL:
				printf("Invalid id %d\n", id);
				break;
			case EIDRM:
				printf("Id %d was already removed\n", id);
				break;
			default:
				printf("Removing id %d failed\n", id);
			}
			return EXIT_FAILURE;

		}
	}
	else 
		usage(stdout);
	return EXIT_SUCCESS;
}
