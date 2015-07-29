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
	sf_sensor_t *sensor_list;
	sf_sensor_t sensor;
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

		sensor_list = (sf_sensor_t *)malloc(count * sizeof(sf_sensor_t));
		result = sf_get_sensor_list(sensor_type_list[i], count, sensor_list);
		if (result < 0) {
			fprintf(stdout, "error: %d, failed to get sensor list\n", result);
			return false;
		}
		for (j = 0; j < count; j++) {
			fprintf(stdout, "No:%d sensor id is %d\n", j, sensor_list[j].sensor_id);
			fprintf(stdout, "\t%d sensor name is %s\n", j, sensor_list[j].sensor_name);
			fprintf(stdout, "\t%d type id is %d\n", j, sensor_list[j].sensor_type.sensor_type_id);
			fprintf(stdout, "\t%d type is %s\n", j, sensor_list[j].sensor_type.sensor_type);
		}
		free(sensor_list);
	}
	free(sensor_type_list);
	return true;
}

