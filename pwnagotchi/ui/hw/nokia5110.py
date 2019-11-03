import logging

import pwnagotchi.ui.fonts as fonts
from pwnagotchi.ui.hw.base import DisplayImpl

class Nokia5110LCD(DisplayImpl):
    def __init__(self, config):
        super(Nokia5110LCD, self).__init__(config, 'waveshare_1')
        self._display = None

    def layout(self):
        fonts.setup(6, 5, 6, 7, 5)
        self._layout['width'] = 84
        self._layout['height'] = 48
        self._layout['face'] = (0, 24)
        self._layout['name'] = (0, 14)
        self._layout['channel'] = (0, 0)
        self._layout['aps'] = (14, 0)
        self._layout['uptime'] = (40, 0)
        self._layout['line1'] = [0, 7, 84, 7]
        self._layout['line2'] = [0, 40, 84, 40]
        self._layout['friend_face'] = (0, 92)
        self._layout['friend_name'] = (40, 94)
        self._layout['shakes'] = (0, 42)
        self._layout['mode'] = (225, 42)
        self._layout['status'] = {
            'pos': (125, 20),
            'font': fonts.Small,
            'max': 20
        }
        return self._layout

    def initialize(self):
        logging.info("initializing lcdhat display")
        from pwnagotchi.ui.hw.libs.monolcd.pcd8544.epd import EPD
        self._display = EPD()
        self._display.clear()

    def render(self, canvas):
        self._display.display(canvas)
        pass
        

    def clear(self):
        self._display.clear()
