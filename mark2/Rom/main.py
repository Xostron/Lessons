from kivymd.app import MDApp
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
from uix.screens.baseclass.callscreen import CallScreen
from kivy.core.window import Window

Window.size = (350, 600)


class PullUp(MDApp):
    def build(self):
        return CallScreen()

a = PullUp()
a.run()