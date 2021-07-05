from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage, Image
from kivy.uix.label import Label

class CarouselApp(App):

    def build(self):
        carousel = Carousel(direction='right')
        image = Image(source="0.gif")
        carousel.add_widget(image)

        return carousel



CarouselApp().run()