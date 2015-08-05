#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <sensor_internal.h>
#include <stdbool.h>
#include <sf_sensor.h>
#include <sf_sensor_data.h>
#include <sensor_common.h>
#include <unistd.h>
#include <string.h>
int
main(int argc, char* argv[])
{
	sf_sensor_id_t sensor_id;
	sf_sensor_data_t data;
	unsigned int count;
	int result;
	int i;
	sensor_id = atoi(argv[1]);
	//initialize sensor environment
	int sensor_type_result = sf_get_sensor_type_count(&count);
	if (sensor_type_result < 0) {
		fprintf(stdout, "error: %d, failed to get sensor type count\n", sensor_type_result);
		return false;
	}
	if(count == 0){
		fprintf(stdout, "No sensor exists in system!\n");
	}
	result = sf_get_sensor_data(sensor_id, &data);
	if(result < 0)
	{
		fprintf(stdout, "error: %d, failed to get sensor data with id %d. Probably because it's not connected.", result, sensor_id);
		return true;
	}
        for(i = 0; i < data.value_count; i++) {
		fprintf(stdout, "value %d: %f\n", i, data.values[i]);
	}
	return false;
}

