from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from flashcard import Flashcard
from main_screen import MainScreen
from settings_screen import SettingsScreen

Config.set('graphics', 'resizable', 1)

Builder.load_file("flashcard.kv")

class MainApp(App):

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name="main"))
        self.sm.add_widget(SettingsScreen(name="settings"))
        self.flashcard = Flashcard(self.sm)
        return self.sm


if __name__ == "__main__":
    MainApp().run()