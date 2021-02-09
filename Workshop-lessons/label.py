
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel


class Main(MDApp):
    def build(self):
        screen = Screen()
        label = MDLabel(text="[b]We are building our first app![/b]",
                        halign='center',
                        font_style='H4',
                        text_color=(1, 0.2, 0.3, 1),
                        theme_text_color='Custom',
                        markup=True)
        screen.add_widget(label)
        return screen


Main().run()
