from kivy.config import Config
from kivy.app import App
from kivy.uix.button import Button

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

from kivy.uix.codeinput import CodeInput
from pygments.lexers.html import HtmlLexer





from kivy.uix.floatlayout import FloatLayout


class myApp(App):

    def build(self):
        f1 = FloatLayout(size=(10, 10))
        f1.add_widget(Button(text='I am Button',
                             font_size=18,
                             on_press=self.btn_press,
                             background_color=[.32, .85, .94, 1],
                             background_normal='',
                             size_hint=(.25, .15),
                             pos=(640/2-640*0.25/2, 480/2-480*0.15/2)))
        return f1

    def btn_press(self, instance):
        print('кнопка нажата')
        instance.text = 'I have already pressed'
        instance.font_size=15


if __name__ == '__main__':
    myApp().run()
