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
        // result of get_sensor_count
        bool sensor_count_return;
	// result of get_sensor_list
        bool sensor_list_return;
        // the count of sensor matched with given type
	int sensor_count;
	int i;
        sf_sensor_type_t sensor_type_t;
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
	result = sf_get_sensor_type_count(&count);
	if (result < 0) {
		fprintf(stdout, "error: %d, failed to get sensor type count\n", result);
		return false;
	}
	if(count == 0){
		fprintf(stdout, "No sensor exists in system!\n");
	}
	fprintf(stdout, "sensor type count is %d\n", count);
        sensor_count_return = sf_get_sensor_count(sensor_type_t, &sensor_count);
        
	if (sensor_count_return < 0) {
		fprintf(stdout, "error: %d, failed to get sensor count\n", sensor_count_return);
		return false;
	}
	if(count == 0 && sensor_count != 0){
		fprintf(stdout, "error: count of sensor should be zero if no sensor exists in system. \n");
		return false;	
	}
	fprintf(stdout, "sensor count is %d\n", sensor_count);
	return true;
}

