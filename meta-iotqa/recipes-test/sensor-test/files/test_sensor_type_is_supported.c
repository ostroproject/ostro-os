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
input 0: sensor unsupported
input 2: sensor supported
*/
int
main(int argc, char* argv[])
{
        // result of get_sensor_count
        bool sensor_count_return;
	sf_sensor_id_t sensor_id;
	sf_sensor_type_t *sensor_type_t;
	int result;
	unsigned int count;
	sf_sensor_type_id_t sensor_type_int = atoi(argv[1]);
	sensor_type_t = (sf_sensor_type_t *)malloc(sizeof(sf_sensor_type_t));	
	sensor_type_t->sensor_type_id = sensor_type_int;
        fprintf(stdout, "input type id: %d\n", sensor_type_t->sensor_type_id);//sensor_type_int);
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
		strcpy(sensor_type_t->sensor_type, "ACCELEROMETER_SENSOR");
		break;
	case 2: 
		strcpy(sensor_type_t->sensor_type, "GEOMAGNETIC_SENSOR");
		break;
        case 3:
		strcpy(sensor_type_t->sensor_type, "LIGHT_SENSOR");
		break;
	case 4:
		strcpy(sensor_type_t->sensor_type, "PROXIMITY_SENSOR");
		break;
	case 5:
		strcpy(sensor_type_t->sensor_type, "THERMOMETER_SENSOR");
		break;
	case 6:
		strcpy(sensor_type_t->sensor_type, "GYROSCOPE_SENSOR");
		break;
        case 7:
		strcpy(sensor_type_t->sensor_type, "PRESSURE_SENSOR");
		break;
	case 24:
		strcpy(sensor_type_t->sensor_type, "TEMPERATURE_SENSOR");
		break;
	default: 
		fprintf(stdout, "error: Unknown sensor");
		return false;
	}
	fprintf(stdout, "input type name: %s\n", sensor_type_t->sensor_type);
	result = sf_get_sensor_type_count(&count);
	//initialize sensor environment
	if (result < 0) {
		fprintf(stdout, "error: %d, failed to get sensor type count\n", result);
		return false;
	}
	fprintf(stdout, "sensor type count is %d\n", count);
	result = sf_sensor_type_is_supported(sensor_type_t);
	if (result < 0) {
		fprintf(stdout, "error: %d, failed to check sensor type is supported or the sensor type is not supported\n", result);
		return false;
	}
	fprintf(stdout, "%s sensor type is supported , the sensor type id is %d\n",
			sensor_type_t->sensor_type,sensor_type_t->sensor_type_id);
	return true;
}

