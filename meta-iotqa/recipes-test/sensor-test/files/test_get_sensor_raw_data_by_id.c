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
	sf_sensor_hw_t hw_info;
	sf_sensor_t sensor;
	sf_sensor_id_t sensor_id;
	sf_sensor_raw_data_t raw_data;
	unsigned int count;
	uint8_t *p;
	int result;
	int i;
	sensor_id = atoi(argv[1]);
	//initialize sensor environment
	int sensor_type_result = sf_get_sensor_type_count(&count);
	if (sensor_type_result < 0) {
		fprintf(stdout, "error: %d, failed to get sensor type count\n", sensor_type_result);
		return false;
	}
	result = sf_connect_sensor(sensor_id);
	if(result < 0)
	{
		fprintf(stdout, "eroor: %d, failed to connect sensor with id %d, pls check sensor id. \n", result, sensor_id);
		return false;
	}
	hw_info.bus_num = 8;
	hw_info.sensor_address = 0x1e;
	hw_info.sensor_register =0x0a;
        result = sf_set_sensor_data_read_method(sensor_id, hw_info);
	if (result <0) {
		fprintf(stdout, "error: %d, failed to set sensor data read method\n", result);
		return false;
	}
	fprintf(stdout, "sensor id %d set read raw data method successfully!\n",
				sensor_id);

	raw_data.size = 10;
	raw_data.raw = (uint8_t *)malloc(sizeof(uint8_t)*10);
	result = sf_get_sensor_raw_data(sensor_id, &raw_data);
	if (result <0) {
		fprintf(stdout, "error: %d, failed to get sensor raw data\n", result);
		return false;
	}
	p = raw_data.raw;
	for (i = 0; i < raw_data.size; i++) {
		fprintf(stdout, "raw value %d: 0x%02x(%c)\n", i, *p, *p);
		p++;
	}

	result = sf_disconnect_sensor(sensor_id);
	if (result <0) {
		fprintf(stdout, "error: %d, failed to disconnect to sensor\n", result);
		return false;
	}
	fprintf(stdout, "Disconnect to sensor id %d successfully!\n",
				sensor_id);

}
