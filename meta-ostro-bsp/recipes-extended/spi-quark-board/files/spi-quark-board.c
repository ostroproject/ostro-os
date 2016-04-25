/*
 * Galileo atmel212b spi board file
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

#define pr_fmt(fmt) "Galileo: " fmt

#include "spi-quark-board.h"

static struct spi_device *dev;
static struct spi_board_info spi_info;
static unsigned int spi_irq;
static u16 spi_master;

static int __init galileo_module_init(void)
{
	struct spi_master *master;
	int err;

	pr_info("module init\n");

	set_spi_quark_board_value(&spi_info, &spi_irq, &spi_master);

	err = -ENODEV;
	master = spi_busnum_to_master(spi_master);
	pr_info("master=%p\n", master);
	if (!master)
		goto out;

	dev = spi_new_device(master, &spi_info);
	pr_info("dev=%p\n", dev);
	if (!dev)
		goto out;

	if (spi_irq) {
		dev->irq = gpio_to_irq(spi_irq);
		irq_set_irq_type(dev->irq, IRQF_TRIGGER_RISING);
	}

	pr_info("802.15.4 chip registered\n");
	err = 0;

 out:
	if (err)
		pr_err("Failed to register SPI device\n");
	return err;
}

static void __exit galileo_module_exit(void)
{
	pr_info("module exit");
	if (dev)
		spi_unregister_device(dev);
}

module_init(galileo_module_init);
module_exit(galileo_module_exit);

MODULE_LICENSE("GPL");
