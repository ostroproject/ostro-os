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
	int sensor_count = 0;
	int i, j;

	result = sf_get_sensor_type_count(&count);
	if (result < 0) {
		fprintf(stdout, "error: %d, failed to get sensor type count\n", result);
		return false;
	}
	if(count == 0){
		fprintf(stdout, "No sensor exists in system!\n");
	}

	total_types = count;

	sensor_type_list = (sf_sensor_type_t *)malloc(count * sizeof(sf_sensor_type_t));

	result = sf_get_sensor_type_list(count, sensor_type_list);
	if (result < 0) {
		fprintf(stdout, "error: %d, failed to get sensor type list\n", result);
		return false;
	}
	for (i = 0; i < count; i++) {
		fprintf(stdout, "%d senor type id is %d ", i, sensor_type_list[i].sensor_type_id);
		fprintf(stdout, "type name is %s\n", sensor_type_list[i].sensor_type);
	}

	// list all sensors
	for (i = 0; i < total_types; i++) {
		result = sf_get_sensor_count(sensor_type_list[i], &count);
		if (result < 0) {
			fprintf(stdout, "error: %d, failed to get sensor count\n", result);
			return false;
		}
		fprintf(stdout, "%d sf_get_sensor_count type=%s count=%d\n", i, sensor_type_list[i].sensor_type, count);
		sensor_count += count;
	}
        fprintf(stdout, "totally %d sensors in systems", sensor_count);
	free(sensor_type_list);
	return true;
}

