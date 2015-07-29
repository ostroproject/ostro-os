#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <sensor_internal.h>
#include <stdbool.h>
#include <sf_sensor.h>
#include <sf_sensor_data.h>
#include <sf_sensor_type.h>
#include <sensor_common.h>
#include <unistd.h>
#include <string.h>
int
main(int argc, char* argv[])
{
	sf_sensor_type_t *sensor_type_list;
	sf_sensor_type_t *sensor_type;
	int result, total_types;
	unsigned int count;
	int i, j;

	result = sf_get_sensor_type_count(&count);
	if (result < 0) {
		fprintf(stdout, "error: %d, failed to get sensor type count\n", result);
		return false;
	}
	if(count == 0){
		fprintf(stdout, "No sensor exists in system!\n");
	}
	fprintf(stdout, "sensor type count is %d\n", count);

	sensor_type_list = (sf_sensor_type_t *)malloc(count * sizeof(sf_sensor_type_t));
	j = count + 1;
	result = sf_get_sensor_type_list(j, sensor_type_list);
	if (result < 0) {
		fprintf(stdout, "error: %d, failed to get sensor type list\n", result);
		return false;
	}
	for (i = 0; i < j; i++) {
		fprintf(stdout, "%d senor type id is %d ", i, sensor_type_list[i].sensor_type_id);
		fprintf(stdout, "type name is %s\n", sensor_type_list[i].sensor_type);
	}
	return true;
}
