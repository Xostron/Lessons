from kivy.app import App
from kivy.core.window import Window

_WIDTH = 400
_HEIGHT = 600
Window.size = (_WIDTH,_HEIGHT)
Window.clearcolor = (.7,.7,.7,0)
Window.set_icon('11.jpg')


from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader

from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage, Image
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout

page = ['У каждого человека свои звезды.\n '
        'Хотел бы я знать, зачем звезды светятся.\n',
        'Наверное, затем, чтобы рано или поздно\n'
        'каждый мог вновь отыскать свою.\n',
        'И самое прекрасное в них то, чего не увидишь\nглазами.',
        'Ты посмотришь ночью на небо,\n'
        'а ведь там будет такая звезда, где я живу,\n'
        'где я смеюсь, – и ты услышишь,\n'
        'что все звёзды смеются.\n'
        'У тебя будут звёзды,\n'
        'которые умеют смеяться!\n',
        '4', '5', '6', '7', '8', '9', '10',
        ]


class CarouselApp(App):
    def myChange(self, instance, value):
        print(self.carousel.index+1)
        pass


    def build(self):
        global page

        self.carousel = Carousel(direction='right')
        self.carousel.bind(on_touch_move=self.myChange)
        self.carousel.scroll_distance = 1
        self.carousel.scroll_timeout = 999
        self.layout = []
        for i in range(10):
            self.layout.append(FloatLayout(size_hint=(1,.55),
                                           pos_hint={'x':0, 'y':.4}))
            source = f'{i}.jpg'
            self.image = Image(source=source,
                               pos_hint={'center_x':.5, 'center_y':.4})
            self.myText = Label(text=page[i],
                                halign='center',
                                valign='top',
                                text_size=[_WIDTH,100],
                                pos_hint={'x':0, 'y':-.8},
                                color='#4B0082')
            self.layout[i].add_widget(self.image)
            self.layout[i].add_widget(self.myText)
            self.carousel.add_widget(self.layout[i])

        return self.carousel


# sound = SoundLoader.load('saib. - Shanghai Nights.mp3')
# if sound:
#     print("Sound found at %s" % sound.source)
#     print("Sound is %.3f seconds" % sound.length)
#     sound.play()

CarouselApp().run()
