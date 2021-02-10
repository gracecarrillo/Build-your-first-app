
from kivy.lang import Builder

from kivymd.app import MDApp

kv = '''
MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "MDToolbar"
        left_action_items: [["menu", lambda x: app.callback()]]

    MDLabel:
        text: "Content"
        halign: "center"
'''


class Main(MDApp):
    def build(self):
        return Builder.load_string(kv)


Main().run()
