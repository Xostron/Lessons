from kivy.app import App
from kivy.config import Config

_WIDTH = 400
_HEIGHT = 600
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', _WIDTH)
Config.set('graphics', 'height', _HEIGHT)

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage, Image
from kivy.uix.label import Label
page = ['У каждого человека свои звезды. '
            'Хотел бы я знать, зачем звезды светятся.',
            'Наверное, затем, чтобы рано или поздно каждый мог вновь отыскать свою.',
            'И самое прекрасное в них то, чего не увидишь глазами.',
            'Ты посмотришь ночью на небо, а ведь там будет такая звезда, где я живу, '
            'где я смеюсь, – и ты услышишь, что все звёзды смеются. '
            'У тебя будут звёзды, которые умеют смеяться!',
        '4', '5', '6', '7', '8', '9', '10',
    ]
class CarouselApp(App):

    def build(self):
        global page
        carousel = Carousel(direction='right')
        for i in range(10):
            if i == 0:
                source = f'{i}.gif'
            else:
                source = f'{i}.jpg'
            image = Image(source=source)
            text = Label(text=page[i])
            image.add_widget(text)
            carousel.add_widget(image)

        return carousel



# sound = SoundLoader.load('saib. - Shanghai Nights.mp3')
# if sound:
#     print("Sound found at %s" % sound.source)
#     print("Sound is %.3f seconds" % sound.length)
#     sound.play()
CarouselApp().run()
















