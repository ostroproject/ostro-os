/*
 * low-speed-spidev board file
 * Copyright (c) 2014, Intel Corporation.
 * All rights reserved.
 *
 * This program is free software; you can redistribute it and/or modify it
 * under the terms and conditions of the GNU General Public License,
 * version 2, as published by the Free Software Foundation.
 *
 * This program is distributed in the hope it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
 * more details.
 *
 * Author: California Sullivan <california.l.sullivan@intel.com>
 */

#define pr_fmt(fmt) "low-speed-spidev: " fmt

#include <linux/platform_device.h>
#include <linux/module.h>
#include <linux/spi/spi.h>

#if (!defined(CONFIG_SPI_SPIDEV_MODULE) && !defined(CONFIG_SPI_SPIDEV))
        #error SPI_SPIDEV is required.
#endif

/* Change these values to what your board uses. */
#define LOW_SPEED_SPIDEV_SPI_BUS 0
#define LOW_SPEED_SPIDEV_SPI_CS 0
#define LOW_SPEED_SPIDEV_MAX_CLK_HZ 1000000

static struct spi_board_info cal_spi_board_info __initdata = {
	.modalias	= "spidev",
	.bus_num	= LOW_SPEED_SPIDEV_SPI_BUS,
	.chip_select	= LOW_SPEED_SPIDEV_SPI_CS,
	.max_speed_hz   = LOW_SPEED_SPIDEV_MAX_CLK_HZ,
};

static struct spi_device *dev;

static int __init low_speed_spidev_module_init(void)
{
	struct spi_master *master;
	int err;

	pr_info("module init\n");

	err = -ENODEV;

	master = spi_busnum_to_master(LOW_SPEED_SPIDEV_SPI_BUS);
	pr_info("master=%p\n", master);
	if (!master)
		goto out;

	dev = spi_new_device(master, &cal_spi_board_info);
	pr_info("dev=%p\n", dev);
	if (!dev)
		goto out;
	pr_info("spidev registered\n");
	err = 0;

 out:
	if (err)
		pr_err("Failed to register SPI device\n");
	return err;
}

static void __exit low_speed_spidev_module_exit(void)
{
	pr_info("module exit");
	if (dev)
		spi_unregister_device(dev);
}

module_init(low_speed_spidev_module_init);
module_exit(low_speed_spidev_module_exit);

MODULE_LICENSE("GPL");
