import os
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivymd.uix.screen import MDScreen
from kivy.animation import Animation
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivymd.color_definitions import colors


# Читаем и загружаем KV файл
with open(os.path.join(os.getcwd(), "uix", "screens", "kv", "callscreen1.kv"),
          encoding="utf-8") as KV:
    Builder.load_string(KV.read())


class CallScreen_1(MDScreen):
    # Флаг для анимации возврата экрана к исходному состоянию.
    def __init__(self, **kwargs):
        super(CallScreen_1, self).__init__(**kwargs)
        Window.bind(on_touch_down=self.mouse_start_pos)
        Window.bind(on_touch_up=self.mouse_reset_pos)
        Window.bind(mouse_pos=self.mouse_pos_my)




    open_call_box = False
    open_call_box1 = False
    open_call_box2 = False
    open_call_box3 = False
    open_call_box4 = False
    open_call_box5 = False
    blur_value = NumericProperty(0)
    start_pos = 0
    event_start_pos = False

    def mouse_start_pos(self,*args):
        if not self.event_start_pos:
            self.event_start_pos = True
            self.start_pos = args[1].pos[1]
            self.alias_y = args[1].pos[1]
            print("Press_down: " + str(self.start_pos))

    def mouse_reset_pos(self,*args):
        if self.event_start_pos:
            self.event_start_pos = False
            self.start_pos = 0
            print("Press up: " + str(self.start_pos))

    def mouse_pos_my(self, window, pos):
        if self.event_start_pos:
            self.alias_y = self.alias_y - pos[1]
            if self.alias_y < 0:
                #self.ids.notes.pos_hint['center_y'] = self.ids.notes.pos_hint['center_y']+0.03
                # new_y = self.ids.notes.property('center_y').get(self) + 5
                if self.ids.notes.pos_hint['center_y']<=0.85:
                    self.ids.notes.myParam = self.ids.notes.myParam+0.02

            else:
                if self.ids.notes.pos_hint['center_y']>=.04:
                    self.ids.notes.myParam = self.ids.notes.myParam-0.02

                # new_y = self.ids.notes.property('center_y').get(self) - 5
                #self.ids.notes.pos_hint['center_y'] = self.ids.notes.pos_hint['center_y'] - 0.03
            self.alias_y = pos[1]

            print('========: '+ str(self.ids.notes.pos_hint['center_y']))
            #self.ids['notes'].pos_hint['center_y'].set(self, int(self.ids.notes.pos_hint['center_y']))
            print('current_y            = '+ str(pos[1]))
            print('current_alias        = ' + str(self.start_pos - pos[1]))
            #print('new_y                = '+ str(new_y))
            print('current_pos_layout   = '+str(self.ids.notes.property('center_y').get(self)))
            print('size_layout   = ' + str(self.ids.notes.property('size').get(self)))
    # def animation_call_button(self, call_button):
    #     if not self.open_call_box1:
    #         Animation(
    #             x=self.center_x - call_button.width / 2,
    #             y=40,
    #             md_bg_color=get_color_from_hex(colors["Red"]["A700"]),
    #             d=0.6,
    #             t="in_out_quad",
    #         ).start(call_button)
    #         self.open_call_box1 = 1
    #     else:
    #         Animation(
    #             y=Window.height * 45 / 100 + call_button.height / 2,
    #             x=self.width - call_button.width - 20,
    #             md_bg_color=get_color_from_hex(colors["Green"]["A700"]),
    #             d=0.6,
    #             t="in_out_quad",).start(call_button)
    #         self.open_call_box1 = 0
    #
    # def animation_title_image(self, title_image):
    #     """
    #     :type title_image: <kivymd.utils.fitimage.FitImage object>
    #     """
    #
    #     if not self.open_call_box:
    #         # Анимация развертывания титульного изображения на весь экран.
    #         Animation(size_hint_y=1, d=0.6, t="in_out_quad").start(title_image)
    #         Animation(blur_value=15, d=0.6, t="in_out_quad").start(self)
    #         self.open_call_box = 1
    #     else:
    #         # Анимация возврата титульного изображения к исходному состоянию.
    #         Animation(size_hint_y=0.45, d=0.6, t="in_out_quad").start(title_image)
    #         Animation(blur_value=0, d=0.6, t="in_out_quad").start(self)
    #         self.open_call_box = 0
    #
    # def animation_list_box(self, list_box):
    #     if not self.open_call_box2:
    #         Animation(
    #             y=-list_box.y,
    #             opacity=0,
    #             d=0.6,
    #             t="in_out_quad"
    #         ).start(list_box)
    #         self.open_call_box2 = 1
    #     else:
    #         Animation(
    #             y=self.height * 45 / 100 - list_box.height / 2,
    #             opacity=1,
    #             d=0.6,
    #             t="in_out_quad"
    #         ).start(list_box)
    #         self.open_call_box2 = 0
    #
    # def animation_round_avatar(self, round_avatar, user_name):
    #     if not self.open_call_box3:
    #         Animation(
    #             x=self.center_x - round_avatar.width / 2,
    #             y=round_avatar.y + 50,
    #             d=0.6,
    #             t="in_out_quad",
    #         ).start(round_avatar)
    #         self.open_call_box3 = 1
    #     else:
    #         Animation(
    #             x=self.center_x - (round_avatar.width + user_name.width + 20) / 2,
    #             y=self.height * 45 / 100 + round_avatar.height,
    #             d=0.6,
    #             t="in_out_quad",
    #         ).start(round_avatar)
    #         self.open_call_box3 = 0
    #
    # def animation_user_name(self, round_avatar, user_name):
    #     if not self.open_call_box4:
    #         Animation(
    #             x=self.center_x - user_name.width / 2,
    #             y=user_name.y - 50,
    #             d=0.6,
    #             t="in_out_quad",
    #         ).start(self.ids.user_name)
    #         self.open_call_box4 = 1
    #     else:
    #         Animation(
    #             x=round_avatar.x +50,
    #             y=round_avatar.center_y - user_name.height - 30,
    #             d=0.6,
    #             t="in_out_quad",
    #         ).start(user_name)
    #         self.open_call_box4 = 0

    # def animation_folder(self, folder, name_folder):
    #     if not self.open_call_box5:
    #         Animation(
    #             opacity=0,
    #             d=.3,
    #             t="in_out_quad",
    #         ).start(name_folder)
    #
    #         Animation(
    #             pos_hint={"center_x": .5, 'center_y':.8},
    #
    #             d=0.3,
    #             t="in_out_quad"
    #         ).start(folder)
    #         self.open_call_box5 = 1
    #         folder.spacing='1dp'
    #         for i in range(1,7):
    #             folder.ids['btn'+str(i)].ids['myIcon'].radius_coef = 2
    #
    #
    #
    #     else:
    #         Animation(
    #             opacity=1,
    #             d=.3,
    #             t="in_out_quad",
    #         ).start(name_folder)
    #
    #         Animation(
    #             pos_hint={"center_x": .5, 'center_y': .5},
    #             d=0.3,
    #             t="in_out_quad"
    #         ).start(folder)
    #         folder.spacing = '24dp'
    #         for i in range(1, 7):
    #             folder.ids['btn' + str(i)].ids['myIcon'].radius_coef = 1
    #
    #         self.open_call_box5 = 0

