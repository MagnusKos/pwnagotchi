# /*****************************************************************************
# * | File        :   config.py
# * | Author      :   Constantine Ganshin
# * | Info        :
# *----------------
# * | This version:   V1.0
# * | Date        :   2019-11-02
# * | Info        :
# ******************************************************************************/
import spidev

# Pin definition
RST_PIN = 22
DC_PIN = 23
BL_PIN = 24

Device_SPI = 1
Device_I2C = 0

Device = Device_SPI
spi = spidev.SpiDev(0, 0)
