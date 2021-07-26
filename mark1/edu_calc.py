from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 340)
Config.set('graphics', 'height', 470)


class Calc(App):
    call_magic = 0

    def upd_lbl(self):
        self.lb1.text = self.formula

    def add_numb(self, instance):
        if self.formula == '0':
            self.formula = ''
        self.formula += instance.text
        self.upd_lbl()

    def add_sign(self, instance):
        if instance.text == 'x':
            self.formula += '*'
        else:
            self.formula += instance.text
        self.upd_lbl()

    def add_result(self, instance):
        self.lb1.text = str(eval(self.lb1.text))
        self.formula = '0'

    def add_magic(self,instance):
        if self.call_magic == 0:
            self.call_magic = 1
            self.grid.spacing = 30
        else:
            self.call_magic = 0
            self.grid.spacing = 3
            print(self.grid.ids)
        print(self.call_magic)

    def build(self):
        self.formula = '0'
        self.box = BoxLayout(orientation='vertical', padding=3)
        self.grid = GridLayout(cols=4, padding=3, spacing=3, size_hint=[1, .6])

        self.grid.add_widget(Button(text='7', on_press=self.add_numb))
        self.grid.add_widget(Button(text='8', on_press=self.add_numb))
        self.grid.add_widget(Button(text='9', on_press=self.add_numb))
        self.grid.add_widget(Button(text='x', on_press=self.add_sign))

        self.grid.add_widget(Button(text='4', on_press=self.add_numb))
        self.grid.add_widget(Button(text='5', on_press=self.add_numb))
        self.grid.add_widget(Button(text='6', on_press=self.add_numb))
        self.grid.add_widget(Button(text='-', on_press=self.add_sign))

        self.grid.add_widget(Button(text='1', on_press=self.add_numb))
        self.grid.add_widget(Button(text='2', on_press=self.add_numb))
        self.grid.add_widget(Button(text='3', on_press=self.add_numb))
        self.grid.add_widget(Button(text='+', on_press=self.add_sign))

        self.grid.add_widget(Button(text='magic', on_press=self.add_magic))
        self.grid.add_widget(Button(text='0', on_press=self.add_numb))
        self.grid.add_widget(Button(text=',', on_press=self.add_numb))
        self.grid.add_widget(Button(text='=', on_press=self.add_result))

        self.lb1 = Label(text='0', font_size=42,
                         halign='right',
                         valign='center',
                         text_size=[340*.7, 470 * .4],
                         size_hint=[.7, 0.4],
                         pos_hint = {'center_x':.5, 'center_y':.5})
        self.box.add_widget(self.lb1)
        self.box.add_widget(self.grid)
        self.box.size_hint = (.7, .7)
        self.box.pos_hint = {'center_x':.5, 'center_y':.5}
        return self.box


if __name__ == '__main__':
    main = Calc().run()
