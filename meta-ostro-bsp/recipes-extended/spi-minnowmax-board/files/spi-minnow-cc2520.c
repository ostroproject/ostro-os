/*
 * MinnowBoard-Max cc2520 spi board file
 * Copyright (c) 2015, Intel Corporation.
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
 */

#define pr_fmt(fmt) "Minnow Max: " fmt

#include <linux/platform_device.h>
#include <linux/module.h>
#include <linux/spi/spi.h>
#include <linux/spi/cc2520.h>

#define CC2520_SPI_MASTER 0

#define CC2520_SPI_CS 0
#define CC2520_MAX_CLK_HZ  8000000

static struct cc2520_platform_data cc2520_data = {
	.fifo = 338,
	.fifop = 339,
	.cca = 340,
	.sfd = 504,
	.reset = 505,
	.vreg  = 464,
};

static struct spi_board_info cc2520_spi_board_info __initdata = {
	.modalias	= "cc2520",
	.max_speed_hz	= CC2520_MAX_CLK_HZ,
	.bus_num	= CC2520_SPI_MASTER,
	.chip_select	= CC2520_SPI_CS,
	.platform_data	= &cc2520_data,
};

static struct spi_device *dev;

static int __init minnow_module_init(void)
{
	struct spi_master *master;
	int err;

	pr_info("module init\n");

	err = -ENODEV;
	master = spi_busnum_to_master(CC2520_SPI_MASTER);
	pr_info("master=%p\n", master);
	if (!master)
		goto out;

	dev = spi_new_device(master, &cc2520_spi_board_info);
	pr_info("dev=%p\n", dev);
	if (!dev)
		goto out;
	pr_info("cc2520 registered\n");
	err = 0;

 out:
	if (err)
		pr_err("Failed to register SPI device\n");
	return err;
}

static void __exit minnow_module_exit(void)
{
	pr_info("module exit");
	if (dev)
		spi_unregister_device(dev);
}

module_init(minnow_module_init);
module_exit(minnow_module_exit);

MODULE_LICENSE("GPL");
