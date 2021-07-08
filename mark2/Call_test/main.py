from kivymd.app import MDApp
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
from uix.screens.baseclass.callscreen import CallScreen


class TestCallScreen(MDApp):
    def build(self):
        return CallScreen()


TestCallScreen().run()