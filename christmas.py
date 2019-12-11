from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.plugins as plugins
import pwnagotchi
import logging
import datetime
import math
import yaml


class Christmas(plugins.Plugin):
    __author__ = 'https://github.com/LoganMD'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'Christmas Countdown timer for pwnagotchi'

    def on_loaded(self):
        logging.info("Christmas Plugin loaded.")
        with open('/etc/pwnagotchi/config.yml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            print(data)

    def on_ui_setup(self, ui):
        with open('/etc/pwnagotchi/config.yml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            if 'memtemp' in data["main"]["plugins"]:
                if 'enabled' in data["main"]["plugins"]["memtemp"]:
                    if data["main"]["plugins"]["memtemp"]["enabled"] == True:
                        memenable = True
                        logging.info("christmas plugin: memtemp is enabled")
                    else:
                        memenable = False
                else:
                    memenable = False
            else:
                memenable = False
        if ui.is_waveshare_v2():
            if memenable == True:
                pos = (135, 80)
            else:
                pos = (200, 80)
            ui.add_element('christmas', LabeledValue(color=BLACK, label='', value='christmas\n',
                                                     position=pos,
                                                     label_font=fonts.Small, text_font=fonts.Small))

    def on_ui_update(self, ui):
        today = datetime.date.today()
        futdate = datetime.date(2019, 12, 25)
        now = datetime.datetime.now()
        mnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
        seconds = math.floor((mnight - now).seconds / 3600)
        days = (futdate - today).days
        ui.set('christmas', "christmas\n%dd %sh" % (days, seconds))
