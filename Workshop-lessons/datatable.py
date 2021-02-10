
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

kv = """
Screen:
    MDRectangleFlatButton:
        text: 'Click me to get table contents'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: app.table()
"""

class Main(MDApp):

    def table(self):
        self.tables =MDDataTable(orientation="lr-tb",
                                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                size_hint=(0.9, 0.6),
                                column_data=[("Food", dp(30)),("Calories", dp(30))],
                                row_data=[("Burger", "300"),("Oats", "50")
                                ]
                                )
        self.tables.open()

    def build(self):
        return Builder.load_string(kv)


Main().run()
