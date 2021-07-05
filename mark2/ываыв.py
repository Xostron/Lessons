from kivy.core.audio import SoundLoader
from kivy.app import App


class mus(App):
    def build(self):
        sound = SoundLoader.load('saib. - Shanghai Nights.mp3')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        return None

mus().run()