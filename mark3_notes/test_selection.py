from kivy.animation import Animation
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivymd.uix.selection import MDSelectionList
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineAvatarListItem, MDList
from kivymd.app import MDApp
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
from kivy.core.window import Window
import os
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivymd.uix.screen import MDScreen
from kivy.animation import Animation
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivymd.color_definitions import colors
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDIconButton, MDFloatingActionButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.widget import Widget
from kivymd.uix.textfield import MDTextField
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.icon_definitions import md_icons
from kivymd.uix.selection import MDSelectionList
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.utils.fitimage import FitImage

with open(file="test.kv", encoding="utf-8") as KV:
    Builder.load_string(KV.read())

class MyItem(TwoLineAvatarListItem):
    pass

class Tool(MDScreen):
    pass

class test_selection(MDList):
    pass


class Example(MDApp):
    overlay_color = get_color_from_hex("#6042e4")
    progress_round_color = get_color_from_hex("#ef514b")

    def build(self):
        screen_main = MDScreen()
        self.tool = Tool()
        scroll = ScrollView()
        #mylayout = MDBoxLayout() #padding=(10,60,10,10)

        self.MySelection = test_selection()
        self.btn = MDFloatingActionButton(icon="pencil-plus",
                                          on_press=self.row_btn)
        for _ in range(10):
            self.MySelection.ids.Loki.add_widget(MyItem())



        scroll.add_widget(self.MySelection)
        #mylayout.add_widget(scroll)
        #mylayout.add_widget(self.MySelection)
        screen_main.add_widget(scroll)
        screen_main.add_widget(self.tool)
        screen_main.add_widget(self.btn)
        return screen_main

    def row_btn(self,instance):
        print("Warhammer")
        print(self.MySelection.ids)
    def set_selection_mode(self, instance_selection_list, mode):
        pass
        print(1)
        # if mode:
        #     md_bg_color = self.overlay_color
        #     left_action_items = [
        #         [
        #             "close",
        #             lambda x: self.MySelection.unselected_all(),
        #         ]
        #     ]
        #     right_action_items = [["trash-can"], ["dots-vertical"]]
        # else:
        #     md_bg_color = (1, 1, 1, 1)
        #     left_action_items = [["menu"]]
        #     right_action_items = [["magnify"], ["dots-vertical"]]
        #     self.tool.title = "Inbox"
        #
        # Animation(md_bg_color=md_bg_color, d=0.2).start(self.tool)
        # self.tool.left_action_items = left_action_items
        # self.tool.right_action_items = right_action_items

    def on_selected(self, selection_list, selection_item):

    # self.tool.title = str(
    #     len(instance_selection_list.get_selected_list_items())
        # )
        print(2)

    def on_unselected(self, selection_list, selection_item):

        print(3)
        # if instance_selection_list.get_selected_list_items():
        #     self.tool.title = str(
        #         len(instance_selection_list.get_selected_list_items())
        #     )


Example().run()