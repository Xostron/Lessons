from kivy.app import App
from kivy.config import Config

_WIDTH = 400
_HEIGHT = 600
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', _WIDTH)
Config.set('graphics', 'height', _HEIGHT)

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader

from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage, Image
from kivy.uix.label import Label
from kivy.properties import AliasProperty

page = ['У каждого человека свои звезды.\n '
        'Хотел бы я знать, зачем звезды светятся.\n',
        'Наверное, затем, чтобы рано или поздно\n'
        'каждый мог вновь отыскать свою.',
        'И самое прекрасное в них то, чего не увидишь\nглазами.',
        'Ты посмотришь ночью на небо,\n'
        'а ведь там будет такая звезда, где я живу,\n'
        'где я смеюсь, – и ты услышишь,\n'
        'что все звёзды смеются.\n'
        'У тебя будут звёзды,\n'
        'которые умеют смеяться!',
        '4', '5', '6', '7', '8', '9', '10',
        ]


class CarouselApp(App):
    def myChange(self, instance, value):
        #print(self.carousel.scroll_distance)
        #print(self.carousel.canvas)
        self.get_right()
        print(self.right)
        pass


    def build(self):
        global page
        self.count = 0

        self.carousel = Carousel(direction='right')
        self.carousel.bind(on_touch_move=self.myChange)
        self.carousel.scroll_distance = 10
        self.carousel.scroll_timeout = 999
        #self.carousel.


        box = BoxLayout(orientation='vertical', padding=3)
        self.text = Label(text=page[self.count],
                          pos=(10, 0),
                          width=300,
                          height=100)
        for i in range(10):
            source = f'{i}.jpg'
            self.image = Image(source=source)
            self.carousel.add_widget(self.image)
        self.slide = self.carousel.next_slide
        box.add_widget(self.carousel)
        box.add_widget(self.text)
        return box


sound = SoundLoader.load('saib. - Shanghai Nights.mp3')
if sound:
    print("Sound found at %s" % sound.source)
    print("Sound is %.3f seconds" % sound.length)
    sound.play()

CarouselApp().run()
