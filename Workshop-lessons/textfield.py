
from kivymd.app import MDApp
from kivy.lang import Builder

textfield_kv = """
Screen:
    MDTextField:
        hint_text: 'Enter you password'
        helper_text: 'Forgot your password?'
        helper_text_mode: "on_focus" 
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
        icon_right: "account-search"
        required: True
"""


class Main(MDApp):
    def build(self):
        return Builder.load_string(textfield_kv)


Main().run()
