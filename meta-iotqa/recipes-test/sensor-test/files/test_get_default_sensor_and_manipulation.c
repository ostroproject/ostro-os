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
/*
input an valid sensor type, such as 2
*/
int
main(int argc, char* argv[])
{
        // result of get_sensor_count
        bool sensor_count_return;
	// result of get_default_sensor
        bool default_sensor_return;
        // the count of sensor matched with given type
	int sensor_count;
	sf_sensor_id_t sensor_id;
	sf_sensor_type_t sensor_type_t;
	sf_sensor_t default_sensor;
	sf_sensor_data_t data;
	sf_sensor_data_t set_data;
	int i;
	int result, count;
	sf_sensor_type_id_t sensor_type_int = atoi(argv[1]);
	sensor_type_t.sensor_type_id = sensor_type_int;
        fprintf(stdout, "input type id: %d\n", sensor_type_t.sensor_type_id);//sensor_type_int);
	switch(sensor_type_int)
	{
/*	case -1: 
		strcpy(sensor_type_t.sensor_type, "ALL_SENSOR");
		break;
	case 0: 
		strcpy(sensor_type_t.sensor_type, "UNKNOWN_SENSOR");
		break; 
	case 1: 
		strcpy(sensor_type_t.sensor_type, "ACCELEROMETER_SENSOR");
		break;
*/
	case 2: 
		strcpy(sensor_type_t.sensor_type, "GEOMAGNETIC_SENSOR");
		break;
	default: 
		fprintf(stdout, "error: Unknown sensor");
		return false;
	}
	fprintf(stdout, "input type name: %s\n", sensor_type_t.sensor_type);
	//initialize sensor environment	
	result = sf_get_sensor_type_count(&count);
	if (result < 0) {
		fprintf(stdout, "error: %d, failed to get sensor type count\n", result);
		return false;
	}
	if(count == 0){
		fprintf(stdout, "No sensor exists in system!\n");
	}
	fprintf(stdout, "sensor type count is %d\n", count);

        default_sensor_return = sf_get_default_sensor(sensor_type_t, &default_sensor);
       	if (default_sensor_return < 0) {
		fprintf(stdout, "error: %d, failed to get default sensor\n", default_sensor_return);
		return false;
	}
	fprintf(stdout, "sf_get_default_sensor type=%s id=%d name=%s\n", sensor_type_t.sensor_type, default_sensor.sensor_id, default_sensor.sensor_name);
	//manipulate the returned default-sensor
        result = sf_connect_sensor(default_sensor.sensor_id);
        if(result < 0) {
		fprintf(stdout, "error: returned default sensor is not correct, check whether it really exist!\n");
		return false;
	}
	result = sf_get_sensor_data(default_sensor.sensor_id, &data);

	fprintf(stdout, "sf_get_sensor_data count=%d timestamp=%llu\n", data.value_count, data.time_stamp);
	for (i = 0; i < data.value_count; i++) {
		fprintf(stdout, "value %d: %f\n", i, data.values[i]);
	}

        // set & get data test for one circle
	set_data.time_stamp = 708970;
	set_data.value_count = 10;
	for (i = 0; i < set_data.value_count; i++) {
		set_data.values[i] = i*i;
	}
	result = sf_set_sensor_data(default_sensor.sensor_id, set_data);
	if (result < 0) {
		sf_disconnect_sensor(default_sensor.sensor_id);
		fprintf(stdout, "Sensor[%d], failed at sf_set_sensor_data ret=%d\n", default_sensor.sensor_id, result);
		return false;
	}
	fprintf(stdout, "sf_set_sensor_data successfully value_count=%d\n", set_data.value_count);

	result = sf_get_sensor_data(default_sensor.sensor_id, &data);
	if (result < 0) {
		sf_disconnect_sensor(default_sensor.sensor_id);
		fprintf(stdout, "Sensor - %d, failed at sf_get_sensor_data after set data.\n",default_sensor.sensor_id);
		return false;
	}
	fprintf(stdout, "sf_get_sensor_data count=%d timestamp=%llu\n", data.value_count, data.time_stamp);
	for (i = 0; i < data.value_count; i++) {
		fprintf(stdout, "value %d: %f\n", i, data.values[i]);
	}
	return true;
}

