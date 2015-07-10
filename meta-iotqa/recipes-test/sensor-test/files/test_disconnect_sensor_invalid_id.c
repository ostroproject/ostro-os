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
	int result, sensor_type_result;
	sensor_id = atoi(argv[1]);
	//initialize sensor environment
	sensor_type_result = sf_get_sensor_type_count(&count);
	if (sensor_type_result < 0) {
		fprintf(stdout, "error: %d, failed to get sensor type count\n", sensor_type_result);
		return false;
	}
	fprintf(stdout, "sensor type count is %d\n", count);
	result = sf_connect_sensor(sensor_id);
	if(result < 0){
		fprintf(stdout, "error: %d, failed to connect to valid sensor id %d \n", result, sensor_id);
		return false;
	}
	fprintf(stdout, "Connect to valid sensor %d successfully. \n", sensor_id);
	result = sf_disconnect_sensor(sensor_id + 1);
	if(result < 0){
		sf_disconnect_sensor(sensor_id);
		fprintf(stdout, "error: %d, fail to disconnect invalid sensor id: %d \n", result, sensor_id + 1);
		return true;
	}
	sf_disconnect_sensor(sensor_id);
	fprintf(stdout, "Disconnect to connected sensor %d successfully. \n", sensor_id);

	return false;
}
