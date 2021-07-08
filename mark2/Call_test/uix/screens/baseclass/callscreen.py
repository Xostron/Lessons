import os
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivymd.uix.screen import MDScreen
from kivy.animation import Animation
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivymd.color_definitions import colors

# Читаем и загружаем KV файл
with open(os.path.join(os.getcwd(), "uix", "screens", "kv", "callscreen.kv"), encoding="utf-8") as KV:
    Builder.load_string(KV.read())


class CallScreen(MDScreen):
    # Флаг для анимации возврата экрана к исходному состоянию.
    open_call_box = False
    open_call_box1 = False
    open_call_box2 = False
    open_call_box3 = False
    open_call_box4 = False
    blur_value = NumericProperty(0)
    def animation_call_button(self, call_button):
        if not self.open_call_box1:
            Animation(
                x=self.center_x - call_button.width / 2,
                y=40,
                md_bg_color=get_color_from_hex(colors["Red"]["A700"]),
                d=0.6,
                t="in_out_quad",
            ).start(call_button)
            self.open_call_box1 = 1
        else:
            Animation(
                y=Window.height * 45 / 100 + call_button.height / 2,
                x=self.width - call_button.width - 20,
                md_bg_color=get_color_from_hex(colors["Green"]["A700"]),
                d=0.6,
                t="in_out_quad",).start(call_button)
            self.open_call_box1 = 0

    def animation_title_image(self, title_image):
        """
        :type title_image: <kivymd.utils.fitimage.FitImage object>
        """

        if not self.open_call_box:
            # Анимация развертывания титульного изображения на весь экран.
            Animation(size_hint_y=1, d=0.6, t="in_out_quad").start(title_image)
            Animation(blur_value=15, d=0.6, t="in_out_quad").start(self)
            self.open_call_box = 1
        else:
            # Анимация возврата титульного изображения к исходному состоянию.
            Animation(size_hint_y=0.45, d=0.6, t="in_out_quad").start(title_image)
            Animation(blur_value=0, d=0.6, t="in_out_quad").start(self)
            self.open_call_box = 0

    def animation_list_box(self, list_box):
        if not self.open_call_box2:
            Animation(
                y=-list_box.y,
                opacity=0,
                d=0.6,
                t="in_out_quad"
            ).start(list_box)
            self.open_call_box2 = 1
        else:
            Animation(
                y=self.height * 45 / 100 - list_box.height / 2,
                opacity=1,
                d=0.6,
                t="in_out_quad"
            ).start(list_box)
            self.open_call_box2 = 0

    def animation_round_avatar(self, round_avatar, user_name):
        if not self.open_call_box3:
            Animation(
                x=self.center_x - round_avatar.width / 2,
                y=round_avatar.y + 50,
                d=0.6,
                t="in_out_quad",
            ).start(round_avatar)
            self.open_call_box3 = 1
        else:
            Animation(
                x=self.center_x - (round_avatar.width + user_name.width + 20) / 2,
                y=self.height * 45 / 100 + round_avatar.height,
                d=0.6,
                t="in_out_quad",
            ).start(round_avatar)
            self.open_call_box3 = 0

    def animation_user_name(self, round_avatar, user_name):
        if not self.open_call_box4:
            Animation(
                x=self.center_x - user_name.width / 2,
                y=user_name.y - 50,
                d=0.6,
                t="in_out_quad",
            ).start(self.ids.user_name)
            self.open_call_box4 = 1
        else:
            Animation(
                x=round_avatar.x +50,
                y=round_avatar.center_y - user_name.height - 20,
                d=0.6,
                t="in_out_quad",
            ).start(user_name)
            self.open_call_box4 = 0

