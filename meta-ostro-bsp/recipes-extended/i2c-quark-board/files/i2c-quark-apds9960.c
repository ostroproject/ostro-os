/*
 * APDS9960 I2C sensor kernel module
 * build command: KDIR=/kernel-source/ make
 * The kernel config should include CONFIG_APDS9960=m
 */

#include <linux/module.h>
#include <linux/gpio.h>
#include <linux/i2c.h>

#define APDS9960_I2C_ADDR		0x39

/* The IRQ pin is connected to GPIO14=IO3
 */
#define APDS9960_I2C_IRQ		14

static struct i2c_board_info i2c_device = {
	I2C_BOARD_INFO("apds9960", APDS9960_I2C_ADDR),
	.irq = -1,
};

static struct i2c_client *i2c_client;
static int __init apds9960_init(void)
{
	struct i2c_adapter *adap = NULL;

	adap = i2c_get_adapter(0);
	if (!adap)
	return -1;

	gpio_request_one(16, GPIOF_OUT_INIT_HIGH, "at86rf230-gpio16");
	i2c_device.irq = gpio_to_irq(APDS9960_I2C_IRQ);
	printk("Create new I2C device on %s \n", adap->name);
	i2c_client = i2c_new_device(adap, &i2c_device);
	return 0;
}

static void __exit apds9960_exit(void)
{
	i2c_unregister_device(i2c_client);
}
MODULE_LICENSE("GPL");
module_init(apds9960_init);
module_exit(apds9960_exit);
