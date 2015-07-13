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
* Verify whether sensor with same name and type can be registered in system or not
*/
int
main(int argc, char* argv[])
{
	char *name = "MiscSensor";
	sf_sensor_type_t type = {MISC_SENSOR, "MISC_SENSOR"};
	sf_sensor_id_t id, dupId;
	int ret, retDup;
	int result;
	sf_sensor_t sensor;

	ret = sf_register_sensor(name, type, &id);
	fprintf(stdout, "sf_register_sensor, id = 0x%x, ret = %d\n", id, ret);

	if (ret < 0) {
		fprintf(stdout, "sf_register_sensor fail!\n", id, ret);
		return false;
	}
	retDup = sf_register_sensor(name, type, &dupId);
	fprintf(stdout, "sf_register_sensor, id = 0x%x, ret = %d\n", dupId, retDup);

	if (retDup < 0) {
		fprintf(stdout, "sf_register_sensor fail!\n", dupId, retDup);
		return false;
	}
	//check both sensors are available in system
	result = sf_get_sensor_by_id(id, &sensor);
	if (result < 0) {
		fprintf(stdout, "Invalid sensor id %d.\n", id);
	} else {
		fprintf(stdout, "[%d] sensor:\n", id);
		fprintf(stdout, "sensor id is 0x%x\n", sensor.sensor_id);
		fprintf(stdout, "sensor name is %s\n", sensor.sensor_name);
		fprintf(stdout, "sensor type id is %d\n", sensor.sensor_type.sensor_type_id);
		fprintf(stdout, "sensor type is %s\n", sensor.sensor_type.sensor_type);
	}
	result = sf_get_sensor_by_id(dupId, &sensor);
	if (result < 0) {
		fprintf(stdout, "Invalid sensor id %d.\n", dupId);
	} else {
		fprintf(stdout, "[%d] sensor:\n", dupId);
		fprintf(stdout, "sensor id is 0x%x\n", sensor.sensor_id);
		fprintf(stdout, "sensor name is %s\n", sensor.sensor_name);
		fprintf(stdout, "sensor type id is %d\n", sensor.sensor_type.sensor_type_id);
		fprintf(stdout, "sensor type is %s\n", sensor.sensor_type.sensor_type);
	}
	ret = sf_unregister_sensor(id);
	fprintf(stdout, "sf_unregister_sensor [%d], ret = %d\n", id, ret);
	ret = sf_unregister_sensor(dupId);
	fprintf(stdout, "sf_unregister_sensor [%d], ret = %d\n", dupId, ret);

	return true;
}

