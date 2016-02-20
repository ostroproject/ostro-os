/*
 * MinnowBoard Max cc2520 spi board file
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

#define pr_fmt(fmt) "MinnowBoard Max: " fmt

#include "spi-minnow-board.h"
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

void set_spi_minnow_board_value(struct spi_board_info *spi_minnow_board_info,
				unsigned int *spi_board_irq, u16 *spi_board_master)
{
	strcpy(spi_minnow_board_info->modalias, "cc2520");
	spi_minnow_board_info->max_speed_hz = CC2520_MAX_CLK_HZ;
	spi_minnow_board_info->bus_num = CC2520_SPI_MASTER;
	spi_minnow_board_info->chip_select = CC2520_SPI_CS;
	spi_minnow_board_info->platform_data  = &cc2520_data;

	*spi_board_irq = 0;
	*spi_board_master = CC2520_SPI_MASTER;
}
EXPORT_SYMBOL(set_spi_minnow_board_value);

static int __init cc2520_module_init(void)
{
	pr_info("module init\n");
	return 0;
}

static void __exit cc2520_module_exit(void)
{
	pr_info("module exit\n");
}

module_init(cc2520_module_init);
module_exit(cc2520_module_exit);

MODULE_LICENSE("GPL");
