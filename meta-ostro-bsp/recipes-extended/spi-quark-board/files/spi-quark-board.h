#ifndef __SPI_QUARK_BOARD_H__
#define __SPI_QUARK_BOARD_H__

#include <linux/platform_device.h>
#include <linux/module.h>
#include <linux/spi/spi.h>
#include <linux/gpio.h>
#include <linux/spi/pxa2xx_spi.h>

void set_spi_quark_board_value(struct spi_board_info *spi_quark_board_info,
				unsigned int *spi_board_irq, u16 *spi_board_master);

#endif
