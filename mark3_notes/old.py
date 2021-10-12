#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import colors kivymd.color_definitions.colors
#:import effect kivy.uix.effectwidget.EffectWidget
#:import HorizontalBlurEffect kivy.uix.effectwidget.HorizontalBlurEffect
#:import VerticalBlurEffect kivy.uix.effectwidget.VerticalBlurEffect
#:import STANDARD_INCREMENT kivymd.material_resources.STANDARD_INCREMENT
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget
#:import MDLabel kivymd.uix.label.MDLabel
#:import Config kivy.config.Config
#:import Button kivy.uix.button
#:import CodeInput kivy.uix.codeinput
#:import KivyLexer kivy.extras.highlight






#"""иконки заметок"""
<Note@MDFloatLayout>
    size_hint: None, None
    size: "160dp", "160dp"
    md_bg_color: .7,.7,.7,1
    my_title:""
    my_text: ""
    full_title: ""
    full_text: ""
    radius: [10, 10, 10, 10]
    canvas:
        Color:
            rgba: 1, 1, 1, 1

        Line:
            width: 1
            rounded_rectangle: (self.x, self.y, self.width, self.height,10)

    MDLabel:
        id: myTitle
        text: root.my_title
        size_hint_y: None
        size_hint_x: None
        height: self.texture_size[1]
        #"""font_style: "Caption""""
        halign: "left"
        #"""theme_text_color: "Custom""""
        text_color: .1, .1, .1, 1
        y: root.y + root.height - self.height - 5
        x: root.x + 5
        md_bg_color: get_color_from_hex(colors["Green"]["A700"])
        -text_size: None, None
        size: self.texture_size
        opacity: 1

    MDLabel:
        id: myText
        text: root.my_text[0:20]+'...'
        size_hint_y: None
        size_hint_x: None
        height: self.texture_size[1]
        font_style: "Caption"
        halign: "left"
        #"""theme_text_color: "Custom""""
        text_color: .1, .1, .1, 1
        y: root.y + root.height - self.height*3.5 - 5
        x: root.x + 5
        md_bg_color: get_color_from_hex(colors["Green"]["A700"])
        -text_size: None, None
        size: self.texture_size
        opacity: 1
    Button:
        icon: '1.jpg'
        x: root.x
        y: root.y
        on_release: root.pushMe(self)
        opacity: 0

#"""Слой для иконок"""
<CallNotes@MDGridLayout>
    id: Imperor
    cols: 2

    adaptive_height: True
    spacing: "10dp"
    padding: [10,70,0,50]
    md_bg_color: .5,.5,.5,1

#"""строка меню для главного экрана"""
<Tool>
    MDToolbar:
        id: tool_bar
        title: "Notes"
        md_bg_color: .7,.7,.7,1
        opposite_colors: True
        #"""left_action_items:  [["menu", lambda x: x]]"""
        #"""right_action_items: [["dots-vertical", lambda x: x]]"""
        y: root.height - self.height

#"""кнопка-иконка"""
<CustomBtn>
#"""Кнопка создать заметку"""
    MDFloatingActionButton:
        id: call_button
        icon: "pencil-plus"
        md_bg_color: app.theme_cls.accent_color
        on_press: root.add_note(self)
        canvas:
            Color:
                rgba: 1, 1, 1, 1
            Line:
                width: 1
                circle:
                    (\
                    self.center_x, \
                    self.center_y, \
                    min(self.width, self.height) / 2, \
                    0, \
                    360, \
                    )

#""""Экран редактирования""""
<Screen2>

#"""Заметка - содержание"""
    MDScreen:
        md_bg_color: .95,.95,.95,1

        MDToolbar:
            id: tool_bar
            title: Input_Title.text
            md_bg_color: .7,.7,.7,1
            opposite_colors: True
            left_action_items:  [["arrow-left", lambda x: root.my_back(self)]]
            right_action_items: [["delete", lambda x: root.my_delete(self)], ["check", lambda x: root.my_back(self)]]
            y: root.height - self.height
            elevation: 10

        TextInput:
            id: Input_Title
            hint_text: "Title..."
            text: "kuji podcast"
            multiline: True
            size_hint: 0.95, 0.15
            pos_hint: {"center_x": 0.5, "center_y":0.8}

        TextInput:
            id: Input_Body
            hint_text: "Note..."
            multiline: True
            size_hint: 0.95, 0.7
            pos_hint: {"center_x": 0.5, "center_y":0.365}

<Selection_note>

    MDSelectionList:
        id: selection_list
        padding: "0dp", "0dp", "0dp", "0dp"
        cols: 2
        spacing: "10dp"
        size_hint_y: None

        overlay_color: app.overlay_color[:-1] + [.2]
        icon_bg_color: app.overlay_color
        progress_round_color: app.progress_round_color
        on_selected: app.onSelected(*args)
        on_unselected: app.onUnselected(*args)
        on_selected_mode: app.setSelectionMode(*args)

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
from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextField
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.icon_definitions import md_icons
from kivymd.uix.selection import MDSelectionList
from kivymd.uix.list import TwoLineAvatarListItem, MDList
from kivy.uix.scrollview import ScrollView

Window.size = (350, 600)

with open(file="callelement.kv", encoding="utf-8") as KV:
    Builder.load_string(KV.read())


class Note(MDFloatLayout):
    """иконки заметок"""

    def __init__(self, **kwargs):
        self.click = False
        super(Note, self).__init__(**kwargs)

    def pushMe(self, instance):
        if not a.flag_selected:
            print("Click on note - ", instance)
            screen_edit_note.ids.Input_Title.text = self.full_title
            screen_edit_note.ids.Input_Body.text = self.full_text
            sm.switch_to(ScreensList[1])
            self.click = True
        elif main_tool.ids.tool_bar.title == 'Notes':
            a.flag_selected = False
        print('=====', a.select.ids.selection_list)


class CallNotes(MDGridLayout):
    """слой с иконками"""
    pass


class Tool(MDScreen):
    """верхняя строка меню - главный экран"""
    pass


class CustomBtn(MDFloatingActionButton):
    """кнопка - создать заметку"""

    def __init__(self, **kwargs):
        self.click = False
        super(CustomBtn, self).__init__(**kwargs)

    def add_note(self, instance):
        """метод - создание заметки"""
        global ScreensList, screen_edit_note
        # добавление заметки на слой
        ListNotes.append(Note())
        sm.switch_to(ScreensList[1])
        print(f"Created {len(ListNotes)}")
        screen_edit_note.ids.Input_Title.text = ""
        screen_edit_note.ids.Input_Body.text = ""
        self.click = True


def ParseShortName(ori, length):
    """
    Функция копирования строки ori в строку res имеющей фиксированную длину length
    c фильтром для символа "переход каретки"
    """
    res = ''
    for i in ori[:length]:
        if i != '\n':
            res += i
        else:
            break
    res += "..."
    return res


class Screen2(MDScreen):
    """
    Экран редактирования заметки
    """

    def my_back(self, instance):
        """
        кнопка перехода на главный экран
        """
        # existing note
        for note in ListNotes:
            if note.click:
                note.click = False
                if note.full_title != self.ids.Input_Title.text:
                    if not self.ids.Input_Title.text:
                        if self.ids.Input_Body.text:

                            note.my_title = ParseShortName(self.ids.Input_Body.text, 10)
                            note.full_title = note.my_title
                        else:
                            myApp.select.ids.selection_list.remove_widget(note)
                            ListNotes.remove(note)
                            break
                    else:
                        note.full_title = self.ids.Input_Title.text
                        note.my_title = ""
                        note.my_title = ParseShortName(note.full_title, 10)
                        print(note.my_title)

                note.full_text = self.ids.Input_Body.text
                note.my_text = ParseShortName(self.ids.Input_Body.text, 20)

        # new note
        if btnAddNote.click:
            btnAddNote.click = False
            if not self.ids.Input_Title.text and not self.ids.Input_Body.text:  # empty
                ListNotes.remove(ListNotes[-1])
                print(f"Empty Notes, so remove it {len(ListNotes)}")
            else:
                if not self.ids.Input_Title.text:
                    self.ids.Input_Title.text = ParseShortName(self.ids.Input_Body.text, 10)

                ListNotes[-1].my_text = ParseShortName(self.ids.Input_Body.text, 20)
                ListNotes[-1].my_title = ParseShortName(self.ids.Input_Title.text, 20)
                ListNotes[-1].full_title = self.ids.Input_Title.text
                ListNotes[-1].full_text = self.ids.Input_Body.text
                a.select.ids.selection_list.add_widget(ListNotes[-1])

        sm.switch_to(ScreensList[0])

    def my_delete(self, instance):
        """
        удалить заметку существующую или новую
        """
        temp_list = []
        for i, note in enumerate(ListNotes):
            if note.click:
                note.click = False
                print('*****', a.select.ids.selection_list.icon)

                print('1@@@@@@', type(a.select.ids.selection_list.children), "\n",
                      a.select.ids.selection_list.children)
                # temp_list = a.select.ids.selection_list.children.copy()
                # del temp_list[i]
                #
                # # a.select.ids.selection_list.remove_widget(note)
                # a.select.ids.selection_list.children = []
                # #a.select.ids.selection_list.clear_widgets()
                # #a.select.clear_widgets()
                # a.select.ids.selection_list.children = temp_list.copy()
                a.select.ids.selection_list.remove_widget(note)
                print('2@@@@@@', a.select.ids.selection_list.children)
                ListNotes.remove(note)
                break

        if btnAddNote.click:
            btnAddNote.click = False
            ListNotes.remove(ListNotes[-1])

        sm.switch_to(ScreensList[0])


class Selection_note(MDList):
    pass


class myApp(MDApp):
    title = "Notes+"
    overlay_color = get_color_from_hex("#6042e4")
    progress_round_color = get_color_from_hex("#ef514b")
    flag_selected = False

    # global layout
    # layout = None
    def build(self):
        # *****************Экран 1 - список заметок*****************
        global MyLayout, ScreensList, sm, screen_edit_note, screen_main, btnAddNote, main_tool
        # return object
        screen_main = MDScreen(md_bg_color=(.5, .5, .5, 1))
        main_tool = Tool()
        # объект скролл для прокручивания по Y слоя self.layout
        self.scroll = ScrollView()
        # инициализация слоя
        self.select = Selection_note()
        for note in ListNotes:
            self.select.ids.selection_list.add_widget(note)

        MyLayout.add_widget(self.select)
        # привязка слоя self.layout к объекту скролл
        self.scroll.add_widget(MyLayout)

        # Кнопка - добавить заметку
        btnAddNote = CustomBtn(x=Window.size[0] - 80, y=50)

        # добавляем элементы на главный экран
        screen_main.add_widget(self.scroll)
        screen_main.add_widget(btnAddNote)
        screen_main.add_widget(main_tool)
        # *****************Экран 2 - редактирование заметки*****************
        screen_edit_note = Screen2()

        # *****************Менеджер экранов*****************
        sm = ScreenManager()
        ScreensList.append(screen_main)
        ScreensList.append(screen_edit_note)
        sm.switch_to(ScreensList[0])
        # возвращаем текщий экран №1
        return sm

    def onSelected(self, selection_list, selection_item):

        main_tool.ids.tool_bar.title = str(len(selection_list.get_selected_list_items()))
        self.flag_selected = True

    def onUnselected(self, selection_list, selection_item):

        if selection_list.get_selected_list_items():
            main_tool.ids.tool_bar.title = str(len(selection_list.get_selected_list_items()))
        if len(selection_list.get_selected_list_items()) == 0:
            main_tool.ids.tool_bar.title = 'Notes'

    def setSelectionMode(self, instance_selection_list, mode):

        if mode:
            md_bg_color = self.overlay_color
            left_action_items = [
                [
                    "close",
                    lambda x: self.MySelection.unselected_all(),
                ]
            ]
            right_action_items = [["trash-can"], ["dots-vertical"]]
        else:
            md_bg_color = (1, 1, 1, 1)
            left_action_items = [["menu"]]
            right_action_items = [["magnify"], ["dots-vertical"]]
            main_tool.ids.tool_bar.title = "Notes"

        Animation(md_bg_color=md_bg_color, d=0.2).start(main_tool.ids.tool_bar)
        main_tool.ids.tool_bar.left_action_items = left_action_items
        main_tool.ids.tool_bar.right_action_items = right_action_items


ListNotes = []  # список объектов-иконок
MyLayout = CallNotes()  # пользовательский слой на котором располагаются иконки заметок

ScreensList = []  # список экранов для ScreenManager

# Главный цикл программы
if __name__ == "__main__":
    print(__name__)
    a = myApp()
    a.run()
