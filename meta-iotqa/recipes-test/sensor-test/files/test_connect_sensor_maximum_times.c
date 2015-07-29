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
	for(i = 0; i <= 64; i++){
		result = sf_connect_sensor(sensor_id);
		if(result < 0 && i == 64)
		{
			fprintf(stdout, "connections to sensor reach allowed maximum.");
			sf_disconnect_sensor(sensor_id);
			return true;
		}
		if(result < 0)
		{
			fprintf(stdout, "eroor: %d, failed to connect sensor with id %d, at time %d. \n", result, sensor_id, i);
			return false;
		} 
		if(result >= 0 && i==64)
		{
			fprintf(stdout, "error: connections to sensor reach allowed maximum but still can be connected.");
			return false;
		}	
	}
}

