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
*/ 
	case 1: 
		strcpy(sensor_type_t.sensor_type, "ACCELEROMETER_SENSOR");
		break;
	case 2: 
		strcpy(sensor_type_t.sensor_type, "GEOMAGNETIC_SENSOR");
		break;
        case 3:
		strcpy(sensor_type_t.sensor_type, "LIGHT_SENSOR");
		break;
	case 4:
		strcpy(sensor_type_t.sensor_type, "PROXIMITY_SENSOR");
		break;
	case 5:
		strcpy(sensor_type_t.sensor_type, "THERMOMETER_SENSOR");
		break;
	case 6:
		strcpy(sensor_type_t.sensor_type, "GYROSCOPE_SENSOR");
		break;
        case 7:
		strcpy(sensor_type_t.sensor_type, "PRESSURE_SENSOR");
		break;
	case 24:
		strcpy(sensor_type_t.sensor_type, "TEMPRERATURE_SENSOR");
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
       	if ( default_sensor_return < 0) {
		fprintf(stdout, "error: %d, failed to get default sensor!!!\n", default_sensor_return);
		return false;
	}
	//check the default sensor whether can be connected
	result = sf_connect_sensor(default_sensor.sensor_id);
        if(result < 0) {
		fprintf(stdout, "error: returned default sensor is not correct, check whether it really exist!\n");
		return false;
	}
	fprintf(stdout, "sf_get_default_sensor type=%s id=%d name=%s\n", sensor_type_t.sensor_type, default_sensor.sensor_id, default_sensor.sensor_name);
	
	return true;
}

