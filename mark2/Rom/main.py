from kivymd.app import MDApp
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
from uix.screens.baseclass.callscreen import CallScreen_1
from kivy.core.window import Window
Window.size = (350, 600)



class PullUp(MDApp):
    title = "al2ms"

    def build(self):
        return CallScreen_1()

a = PullUp()
a.run()