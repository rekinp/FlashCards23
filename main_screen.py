from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from flashcard import IMAGE_BACKGROUND

WINDOW_WIDTH = 380
WINDOW_HEIGHT = 680

class MainScreen(Screen):
    image_source = StringProperty(IMAGE_BACKGROUND)
    menu_image_source = StringProperty('resources/images/menu_icon.png')
    font_name_menu = StringProperty("Arial")
    font_name_words = StringProperty("Georgia")

    def on_pre_enter(self):
        Window.size = (WINDOW_WIDTH,WINDOW_HEIGHT)