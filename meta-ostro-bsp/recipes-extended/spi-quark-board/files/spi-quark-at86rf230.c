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

#include <linux/spi/at86rf230.h>

#define AT86RF_SPI_MASTER 169

#define AT86RF_SPI_CS 0
#define AT86RF_MAX_CLK_HZ  5000000
#define AT86RF_IRQ 14

static struct pxa2xx_spi_chip qrk_ffrd_spi_1_cs_0 = {
	.gpio_cs = 10,
};

static struct at86rf230_platform_data at86rf230_data = {
	.rstn = 12,
	.slp_tr = 13,
	.xtal_trim = 0x2,
	.dig2 = 0,
};

void set_spi_quark_board_value(struct spi_board_info *spi_quark_board_info,
				unsigned int *spi_board_irq, u16 *spi_board_master)
{
	strcpy(spi_quark_board_info->modalias, "at86rf212b");
	spi_quark_board_info->max_speed_hz = AT86RF_MAX_CLK_HZ;
	spi_quark_board_info->bus_num = AT86RF_SPI_MASTER;
	spi_quark_board_info->chip_select = AT86RF_SPI_CS;
	spi_quark_board_info->platform_data = &at86rf230_data;
	spi_quark_board_info->controller_data = &qrk_ffrd_spi_1_cs_0;

	*spi_board_irq = AT86RF_IRQ;
	*spi_board_master = AT86RF_SPI_MASTER;
}
EXPORT_SYMBOL(set_spi_quark_board_value);

static int __init at86rf230_quark_module_init(void)
{
	pr_info("module init\n");
	return 0;
}

static void __exit at86rf230_quark_module_exit(void)
{
	pr_info("module exit\n");
}

module_init(at86rf230_quark_module_init);
module_exit(at86rf230_quark_module_exit);

MODULE_LICENSE("GPL");
