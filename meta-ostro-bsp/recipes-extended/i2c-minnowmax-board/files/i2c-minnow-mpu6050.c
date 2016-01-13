/*
 * MinnowBoard-Max MPU-6050 I2C sensor test file
 * build command: KDIR=/kernel-source/ make
 * The kernel config should include CONFIG_INV_MPU6050_IIO=m
 */

#include <linux/module.h>
#include <linux/gpio.h>
#include <linux/i2c.h>
#include <linux/platform_data/invensense_mpu6050.h>

#define MPU6050_I2C_ADDR		0x68

/* The MPU-6050 IRQ pin is connected to pin25(GPIO_S5_2) of LSE connector,
 * On Linux >=3.18, it is GPIO 340
 * For more information, visit the below
 * http://www.elinux.org/Minnowboard:MinnowMax#Low_Speed_Expansion_.28Top.29
 */
#define MPU6050_I2C_IRQ		340

static struct inv_mpu6050_platform_data mpu_data = {
	.orientation = {0, 1, 0, 1, 0, 0, 0, 0, -1},
};

static struct i2c_board_info mpu6050_accel_device = {
	I2C_BOARD_INFO("mpu6050", MPU6050_I2C_ADDR),
	.irq = -1,
	.platform_data = &mpu_data,
};

static struct i2c_client *i2c_client;
static int __init mpu6050_init(void)
{
	int i = 0;
	struct i2c_adapter *adap = NULL;

	for (i = 0; i < 10; i++) {
		adap = i2c_get_adapter(i);
		if (!adap)
			return -1;

		if (!strcmp(adap->name, "Synopsys DesignWare I2C adapter"))
			break;
	}

	mpu6050_accel_device.irq = gpio_to_irq(MPU6050_I2C_IRQ);

	i2c_client = i2c_new_device(adap, &mpu6050_accel_device);
	return 0;
}

static void __exit mpu6050_exit(void)
{
	i2c_unregister_device(i2c_client);
}
MODULE_LICENSE("GPL");
module_init(mpu6050_init);
module_exit(mpu6050_exit);
