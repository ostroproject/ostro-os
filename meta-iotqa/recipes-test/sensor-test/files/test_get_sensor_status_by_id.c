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
/**
return code:
2: fail to connect sensor, probably because sensor_id is invalid
1: fail to get sensor status
0: get sensor status successfully
**/
int
main(int argc, char* argv[])
{
	sf_sensor_id_t sensor_id;
	sf_sensor_status_t sensor_status;
	char status_desc[20];
	unsigned int count;
	sensor_id = atoi(argv[1]);
	//initialize sensor data
	int sensor_type_result = sf_get_sensor_type_count(&count);
	if (sensor_type_result < 0) {
		fprintf(stdout, "error: %d, failed to get sensor type count\n", sensor_type_result);
		return false;
	}
	if(count == 0){
		fprintf(stdout, "No sensor exists in system!\n");
	}
	fprintf(stdout, "sensor type count is %d\n", count);
	//connect to sensor firstly

	int result = sf_connect_sensor(sensor_id);
	if (result <0) {
		fprintf(stdout, "error: %d, failed to connect to sensor. check sensor_id is valid.\n", result);
		return 2;
	}

	fprintf(stdout, "Connect to sensor id %d successfully!\n", sensor_id);

	result = sf_get_sensor_status(sensor_id, &sensor_status);
        if (result < 0) {
		fprintf(stdout, "error: %d, failed to get sensor status\n", result);
		return 0;
	}
	
        if (sensor_status == SF_SENSOR_READY) 
		strcpy(status_desc, "SF_SENSOR_READY");
	if (sensor_status == SF_SENSOR_RUNNING)
		strcpy(status_desc, "SF_SENSOR_RUNNING");
/*	result = sf_connect_sensor(sensor_id);
	if (result <0) {
		fprintf(stdout, "error: %d, failed to connect to sensor\n", result);
		return 2;
	} */
	sf_disconnect_sensor(sensor_id);
	fprintf(stdout, "sf_get_sensor_status_by_id [%d] sensor:\n", sensor_id);
	fprintf(stdout, "\tid is %d\n", sensor_id);
	fprintf(stdout, "\tstatus is %s\n", status_desc);
	return 1;
}
