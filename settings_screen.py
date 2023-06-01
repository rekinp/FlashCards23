
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from flashcard import IMAGE_BACKGROUND


class SettingsScreen(Screen):
    image_source = StringProperty(IMAGE_BACKGROUND)
    font_size = StringProperty("21dp")
    font_name = StringProperty("Arial")