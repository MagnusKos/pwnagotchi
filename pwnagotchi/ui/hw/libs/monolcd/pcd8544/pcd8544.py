import spidev
import time
import RPi.GPIO as GPIO
from PIL import Image

class PCD8544(object):
    def __init__(self, spi, rst=27, dc=25, bl=24):
        self.width = 84
        self.height = 48
        # Initialize DC RST pin
        self._dc = dc
        self._rst = rst
        self._bl = bl
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self._dc, GPIO.OUT)
        GPIO.setup(self._rst, GPIO.OUT)
        GPIO.setup(self._bl, GPIO.OUT)
        GPIO.output(self._bl, GPIO.HIGH)
        # Initialize SPI
        self._spi = spi
        self._spi.max_speed_hz = 4000000
        # Horizontal mode
        self.command(0x20)

    def command(self, cmd):
        GPIO.output(self._dc, GPIO.LOW)
        self._spi.writebytes([cmd])

    def data(self, val):
        GPIO.output(self._dc, GPIO.HIGH)
        self._spi.writebytes([val])

    def set_contrast(self, contrast):
        if ( 0x80 <= contrast < 0xFF):
            self.command([0x21, 0x14, contrast, 0x20, 0x0c])

    def draw_image(self, image):
        if image.mode != '1':
            raise ValueError('Image must be b/w.')
        buffer = []
        for row in range(6):
            for x in range(84):
                bits = 0
                for bit in [0, 1, 2, 3, 4, 5, 6, 7]:
                    bits = bits << 1
                    bits |= 1 if image[(x, row*8+7-bit)] == 0 else 0
                buffer[index] = bits
                index += 1
        self.gotozero()
        self.command(0x22)
        self.data(buffer)
        self.command(0x20)

    def gotozero(self):
        self.command([0x80, 0x40])

    def reset(self):
        GPIO.output(self._rst, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(self._rst, GPIO.HIGH)