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

/* The MPU-6050 IRQ pin is connected to GPIO12=IO3
 */
#define MPU6050_I2C_IRQ		12

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
	int ret;
	int i = 0;
	struct i2c_adapter *adap = NULL;

	for (i = 1; i < 8; i++) {
		adap = i2c_get_adapter(i);
		if (!adap)
			return -1;

		if (!strcmp(adap->name, "i2c-designware-6"))
			break;
	}

	if (!gpio_is_valid(MPU6050_I2C_IRQ)) {
		printk(KERN_WARNING "GPIO#%d is not valid\n", MPU6050_I2C_IRQ);
		return -EINVAL;
	}

	ret = gpio_request_one(MPU6050_I2C_IRQ, GPIOF_IN, "mpu6050-irq");
	if (ret) {
		printk(KERN_WARNING "failed to request GPIO#%d\n", MPU6050_I2C_IRQ);
		return ret;
	}
	
	mpu6050_accel_device.irq = gpio_to_irq(MPU6050_I2C_IRQ);
	i2c_client = i2c_new_device(adap, &mpu6050_accel_device);
	return 0;
}

static void __exit mpu6050_exit(void)
{
	i2c_unregister_device(i2c_client);
	gpio_free(MPU6050_I2C_IRQ);	
}
MODULE_LICENSE("GPL");
module_init(mpu6050_init);
module_exit(mpu6050_exit);
