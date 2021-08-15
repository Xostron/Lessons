from plyer import filechooser
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDToolbar

#:import MDFloatLayout from kivy.uix.floatlayout.MDFloatLayout
kv = \
"""
MDFloatLayout:
    Image:
        id: img
    MDRaisedButton:
        text: "Upload"
        pos_hint: {"center_x":.5, "center_y":.4}
        on_release:
            app.file_chooser()
    MDLabel:
        id: selected_path
        text:""
        halign:"center"
"""




class myApp(MDApp):

    def build(self):
        return Builder.load_string(kv)
    def file_chooser(self):
        filechooser.open_file(on_selection=self.selected)
    def selected(self, selection):
        if selection:
            self.root.ids.img.source = selection[0]



myApp().run()
