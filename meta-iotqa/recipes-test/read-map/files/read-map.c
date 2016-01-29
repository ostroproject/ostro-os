#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	FILE *f;
	char line[256];
	char *ptr;
	f = fopen("/proc/self/maps", "r");
	if( f == NULL )
	{
		perror("Error opening maps file\n");
		exit(1);
	}

	fgets(line, 256, f); 
	unsigned long long start = strtol(line, &ptr , 16 );
	printf("start is %llx\n", start);
	// pointing to memory outside of map
	char *wr = (char *) (start - 100);
	// assigning random value 4 outside of map
	// should create a segfault
	*wr = 4;
	int val = *wr;
	printf("val is %d\n", val);
	return 0;
}
