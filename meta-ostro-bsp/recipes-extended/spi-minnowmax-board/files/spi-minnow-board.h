#ifndef __SPI_MINNOW_BOARD_H__
#define __SPI_MINNOW_BOARD_H__

#include <linux/platform_device.h>
#include <linux/module.h>
#include <linux/spi/spi.h>
#include <linux/gpio.h>

void set_spi_minnow_board_value(struct spi_board_info *spi_minnow_board_info,
                                unsigned int *spi_board_irq, u16 *spi_board_master);

#endif
