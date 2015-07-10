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
	sf_sensor_id_t sensor_id;
	sf_sensor_t sensor;
	unsigned int count;
	sensor_id = atoi(argv[1]);
	//initialize sensor environment
	int sensor_type_result = sf_get_sensor_type_count(&count);
	if (sensor_type_result < 0) {
		fprintf(stdout, "error: %d, failed to get sensor type count\n", sensor_type_result);
		return false;
	}
	fprintf(stdout, "sensor type count is %d\n", count);
	int result = sf_get_sensor_by_id(sensor_id, &sensor);
	if (result < 0) {
		fprintf(stdout, "Invalid sensor id %d.\n", sensor_id);
		return false;
	} else {
		fprintf(stdout, "sf_get_sensor_by_id [%d] sensor:\n", sensor_id);
		fprintf(stdout, "\tid is %d\n", sensor.sensor_id);
		fprintf(stdout, "\tname is %s\n", sensor.sensor_name);
		fprintf(stdout, "\ttype id is %d\n", sensor.sensor_type.sensor_type_id);
		fprintf(stdout, "\ttype is %s\n", sensor.sensor_type.sensor_type);
		return true;
	}

}

