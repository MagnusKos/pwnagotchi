from . import PCD8544
from . import config
from PIL import Image
from PIL import ImageOps


class EPD(object):
    def __init__(self):
        self.reset_pin = config.RST_PIN
        self.dc_pin = config.DC_PIN
        self.width = 84
        self.height = 48
        self.pcd8544 = PCD8544.PCD8544(config.spi, config.RST_PIN, config.DC_PIN, config.BL_PIN)

    @property
    def size(self):
        return (self.width, self.height)

    def init(self):
        self.pcd8544.init()

    def clear(self):
        self.pcd8544.reset()

    def display(self, image):
        if image.mode != "1":
            image = ImageOps.grayscale(image).convert("1", dither=Image.FLOYDSTEINBERG)
        if image.size != self.size:
            pass
        self.pcd8544.draw_image(image)
