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
#define AT86RF_MAX_CLK_HZ  3000000
#define AT86RF_IRQ 14

static struct gpio quark_at86rf_gpios[] = {
	// config gpio12=IO1=nRST
	{28, GPIOF_OUT_INIT_LOW, "at86rf230-gpio28"},
	{29, GPIOF_IN, "at86rf230-gpio29"},
	{45, GPIOF_OUT_INIT_LOW, "at86rf230-gpio45"},

	// config gpio13=IO2=SLP_TR
	{34, GPIOF_OUT_INIT_LOW, "at86rf230-gpio34"},
	{35, GPIOF_IN, "at86rf230-gpio35"},
	{77, GPIOF_OUT_INIT_LOW, "at86rf230-gpio77"},

	// config gpio14=IO3=IRQ
	{16, GPIOF_OUT_INIT_HIGH, "at86rf230-gpio16"},
	{AT86RF_IRQ, GPIOF_IN, "at86rf230-irq"},
	{17, GPIOF_IN, "at86rf230-gpio17"},
	{76, GPIOF_OUT_INIT_LOW, "at86rf230-gpio76"},
	{64, GPIOF_OUT_INIT_LOW, "at86rf230-gpio64"},

	// config IO10=nCS
	{26, GPIOF_OUT_INIT_LOW, "at86rf230-gpio26"},
	{74, GPIOF_OUT_INIT_LOW, "at86rf230-gpio74"},
	{27, GPIOF_IN, "at86rf230-gpio27"},

	// config IO11=MOSI
	{24, GPIOF_OUT_INIT_LOW, "at86rf230-gpio24"},
	{44, GPIOF_OUT_INIT_HIGH, "at86rf230-gpio44"},
	{72, GPIOF_OUT_INIT_LOW, "at86rf230-gpio72"},
	{25, GPIOF_IN, "at86rf230-gpio25"},

	// config IO12=MISO
	{42, GPIOF_OUT_INIT_HIGH, "at86rf230-gpio42"},
	{43, GPIOF_IN, "at86rf230-gpio43"},

	// config IO13=CLK
	{30, GPIOF_OUT_INIT_LOW, "at86rf230-gpio30"},
	{46, GPIOF_OUT_INIT_HIGH, "at86rf230-gpio46"},
	{31, GPIOF_IN, "at86rf230-gpio31"},
};

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
	pr_info("Load at86rf230 clock %dHz\n", AT86RF_MAX_CLK_HZ);
	strcpy(spi_quark_board_info->modalias, "at86rf230");
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
	int i;
	struct gpio *array = quark_at86rf_gpios;

	pr_info("module init config related GPIO pins\n");

	for (i = 0; i < ARRAY_SIZE(quark_at86rf_gpios); i++, array++) {
		gpio_request_one(array->gpio, array->flags, array->label);
	}

	return 0;
}

static void __exit at86rf230_quark_module_exit(void)
{
	pr_info("module exit\n");
	gpio_free_array(quark_at86rf_gpios, ARRAY_SIZE(quark_at86rf_gpios));
}

module_init(at86rf230_quark_module_init);
module_exit(at86rf230_quark_module_exit);

MODULE_LICENSE("GPL");
