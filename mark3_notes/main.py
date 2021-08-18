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
Window.size = (350, 600)

with open(file="callelement.kv", encoding="utf-8") as KV:
    Builder.load_string(KV.read())


class Note(MDFloatLayout):
    """иконки заметок"""
    pass
    def pushMe(self, instance):
        print(2, instance)

class CallNotes(MDGridLayout):
    """слой с иконками"""
    pass


class Tool(MDScreen):
    """верхняя строка меню"""
    pass


class CustomBtn(MDFloatingActionButton):
    """кнопка - иконка"""
    pass

    def add_note(self, instance):
        global MyLayout, ScreensList, sm
        # добавление заметки на слой
        ListNotes.append(Note())
        MyLayout.add_widget(ListNotes[len(ListNotes)-1])
        sm.switch_to(ScreensList[1])


class Screen2(MDScreen):
    pass


class PullUp(MDApp):
    title = "Notes"
    #global layout
    #layout = None
    def build(self):

        #*****************Screen_main*****************
        global MyLayout, ScreensList, sm
        # return object
        self.screen_main = MDScreen(md_bg_color=(.5,.5,.5,1))
        # объект скролл для прокручивания по Y слоя self.layout
        self.scroll = ScrollView()
        # инициализация слоя
        for note in ListNotes:
            MyLayout.add_widget(note)
        # привязка слоя self.layout к объекту скролл
        self.scroll.add_widget(MyLayout)
        # Кнопка - добавить заметку
        self.btnAddNote = CustomBtn(x=Window.size[0]-80, y=50)
        # добавляем элементы на главный экран
        self.screen_main.add_widget(self.scroll)
        self.screen_main.add_widget(self.btnAddNote)
        # *****************Screen_main*****************

        # *****************Screen_edit_note*****************
        # экран редактирования заметки
        self.screen_edit_note = Screen2()

        #self.screen_edit_note.add_widget(self.screen2)
        # *****************Screen_edit_note*****************

        sm = ScreenManager()
        ScreensList.append(self.screen_main)
        ScreensList.append(self.screen_edit_note)
        sm.switch_to(ScreensList[0])
        # возвращаем экран
        return sm



# пользовательский слой на котором располагаются иконки заметок
ListNotes = []
MyLayout = CallNotes()

#
ScreensList = []



# Главный цикл программы
if __name__ == "__main__":
    print(__name__)
    a = PullUp()
    a.run()
