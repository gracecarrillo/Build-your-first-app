
from kivymd.app import MDApp
from kivy.lang import Builder

class Main(MDApp):

    def build(self):
        return Builder.load_file('lists.kv')

Main().run()
