from kivy.app import App
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 200)

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class MainApp(App):

    def build(self):
        # a = AnchorLayout(anchor_x='left',anchor_y='top')
        box = BoxLayout(orientation='vertical', padding=3, size_hint=[1, 1])
        # grid1 = GridLayout(rows=4, padding=3, spacing=3, size_hint=[1, 1])
        # grid2 = GridLayout(rows=4, padding=3, spacing=3, size_hint=[1, 1])
        in1 = TextInput(text='Введите путь до книги...')
        in2 = TextInput(text='Введите путь сохранения файла...')
        box.add_widget(in1)
        box.add_widget(in2)

        my_widget = Widget()
        # text1 = Label(text='Выбрано слов:', pos=(5, 50), text_size=(100,44),halign="left", valign='center')
        # text2 = Label(text='из:', pos=(200, 100))
        # words = TextInput(text='0', pos=(110, 100))
        # totalWords = TextInput(text='0', pos=(297, 100))
        text1 = Label(text='Выбрано слов:',
                      pos=(8, 25),
                      color=[1,0,0,1])
        text2 = Label(text='из:',
                      pos=(200, 25),
                      color=[1,0,0,1])
        words = TextInput(text='0', multiline=False, halign='center', padding_y=15,
                          pos=(120, 52),
                          width=107,
                          height=48)
        totalWords = TextInput(text='0', multiline=False, halign='center', padding_y=15,
                               pos=(270, 52),
                               width=127,
                               height=48)
        my_widget.add_widget(text1)
        my_widget.add_widget(words)
        my_widget.add_widget(text2)
        my_widget.add_widget(totalWords)

        box.add_widget(my_widget)

        btn_start = Button(text='Start', background_color=[0.5,0.5,1,1])
        box.add_widget(btn_start)



        return box


if __name__ == '__main__':
    main = MainApp().run()
