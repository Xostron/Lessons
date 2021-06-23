from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput


class myPrj(App):
    def build(self):




        a1 = AnchorLayout(anchor_x='center', anchor_y='center')
        # a1.add_widget(Button(text='A1', size_hint=[.5,.5]))

        # g1 = GridLayout(rows=5, padding=25, spacing=5)
        # for i in range(10):
        #     g1.add_widget(Button(text=f'G{i+1}'))


        b1 = BoxLayout(orientation='vertical', size_hint=[.5, .5], spacing=10)
        b1.add_widget(TextInput(text='Login'))
        b1.add_widget(TextInput(text='Password'))
        b1.add_widget(Button(text='Login'))
        a1.add_widget(b1)
        return a1


if __name__ == '__main__':
    myPrj().run()