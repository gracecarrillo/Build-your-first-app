
from kivymd.app import MDApp
from kivy.lang import Builder

button_kv = """
Screen:
    MDLabel:
        text: ""
        id: txt
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
    MDRaisedButton:
        text: 'Action Button'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press:
            app.action()
    MDRoundFlatButton:
        text: 'MDRoundFlatButton'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
    MDRectangleFlatButton:
        text: 'MDRectangleFlatButton'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
    MDRectangleFlatIconButton:
        text: 'MDRectangleFlatIconButton'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        width: dp(230)
        icon: 'google'
    MDFillRoundFlatIconButton:
        text: 'MDFillRoundFlatIconButton'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        width: dp(230)
        icon: 'google'
    MDFloatingActionButtonSpeedDial:
        data: app.data
        rotation_root_button: True
"""


class Main(MDApp):
    data = {
        'language-python': 'Python',
        'language-php': 'PHP',
        'language-cpp': 'C++',
    }

    def action(self):
        label = self.root.ids.txt
        label.text = "This text is displayed after pressing button"

    def build(self):
        return Builder.load_string(button_kv)


Main().run()
