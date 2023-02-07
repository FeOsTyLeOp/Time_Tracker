from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class TimeTrackerApp(MDApp):
    def build(self):
        return MDLabel(text="Welcome to Time Tracker", halign="center")


TimeTrackerApp().run()