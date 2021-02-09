
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty


class Main(MDApp):
    in_class = ObjectProperty(None)

    def build(self):
        return Builder.load_file('basic_auth.kv')

    def auth(self):
        if self.root.in_class.text == 'root':
            label = self.root.ids.show
            label.text = 'Sucess'
        else:
            label = self.root.ids.show
            label.text = 'Fail'


Main().run()
