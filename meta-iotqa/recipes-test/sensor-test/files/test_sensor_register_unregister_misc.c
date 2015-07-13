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
* test api sf_register_sensor and sf_unregister_sensor using a misc sensor
*/
int
main(int argc, char* argv[])
{
	char *name = "MiscSensor";
	sf_sensor_type_t type = {MISC_SENSOR, "MISC_SENSOR"};
	sf_sensor_id_t id;
	int ret;
	int result;
	sf_sensor_t sensor;

	ret = sf_register_sensor(name, type, &id);
	fprintf(stdout, "sf_register_sensor, id = 0x%x, ret = %d\n", id, ret);

	if (ret < 0) {
		fprintf(stdout, "sf_register_sensor fail!\n", id, ret);
		return false;
	}
	//check sensor is available in system
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
	//check sensor can be connected
	result = sf_connect_sensor(id);
	if (result <0) {
		fprintf(stdout, "error: %d, failed to connect to sensor\n", result);
		return false;
	}

	fprintf(stdout, "Connect to sensor id %d successfully!\n", id);

	result = sf_disconnect_sensor(id);
	if (result <0) {
		fprintf(stdout, "error: %d, failed to disconnect to sensor\n", result);
		return false;
	}
	fprintf(stdout, "Disconnect to sensor id %d successfully!\n", id);

	ret = sf_unregister_sensor(id);
	fprintf(stdout, "sf_unregister_sensor, ret = %d\n", ret);

	return true;
}

