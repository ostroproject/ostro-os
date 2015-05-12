#include "mraa.h"
int
main(int argc, char** argv)
{
char* board_name = mraa_get_platform_name();
fprintf(stdout, "hello mraa\n Version: %s\n Running on %s\n", mraa_get_version(), board_name);
mraa_deinit();
return MRAA_SUCCESS;
}

