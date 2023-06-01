from kivy.app import App
from itertools import cycle
from application_data import ApplicationData

LANGUAGE_ENGLISH = "ENGLISH"
LANGUAGE_GERMAN = "DEUTSCH"
LANGUAGE_POLISH = "POLSKI"
LANGUAGES_LIST = [LANGUAGE_ENGLISH, LANGUAGE_POLISH]
IMAGE_BACKGROUND_ENGLISH = "resources/images/background_english.png"
IMAGE_BACKGROUND = "resources/images/background.png"
DEFAULT_FONT_COLOR = (30/255, 30/255, 30/255, 1)

# Creating Layout class
class Flashcard:
    def __init__(self, screen_manager):
        self.sm = screen_manager
        self.app_data = ApplicationData()
        self.set_words(self.app_data.current_words)
        self.update_main_ui()
        self.remove_next_word = True

    def set_words(self, current_words):
        words = current_words.split(",")
        self.german_word = words[0]
        self.english_word = words[1].strip()
        self.polish_word = words[2].strip()
        self.word_translations = {LANGUAGE_ENGLISH: self.english_word,
                                  LANGUAGE_POLISH: self.polish_word
        }
        self.LANGUAGES_LIST_CYCLE = cycle(LANGUAGES_LIST)

    def update_main_ui(self):
        main_screen = self.sm.get_screen("main")
        main_screen.ids.label_counter.text = f"{len(self.app_data.working_dictionary)}/{self.app_data.NUMBER_OF_WORDS_LOADED}"
        main_screen.ids.label_language.text = LANGUAGE_GERMAN
        main_screen.ids.label_word.text = self.german_word

    def yes_button_clicked(self):
        if self.remove_next_word:
            self.app_data.remove_current_word_from_dictionary()
            self.app_data.save_words_to_learn()
        self.set_new_words()
        self.update_main_ui()
        self.change_image(IMAGE_BACKGROUND)
        self.change_label_word_font_color(DEFAULT_FONT_COLOR)
        self.remove_next_word = True

    def no_button_clicked(self):
        current_language = next(self.LANGUAGES_LIST_CYCLE)
        self.update_language_label(current_language)
        self.update_word_label(self.word_translations[current_language])
        self.change_image(IMAGE_BACKGROUND_ENGLISH)
        self.change_label_word_font_color("white")
        self.remove_next_word = False

    def next_lesson_button_clicked(self):
        self.app_data.set_word_package_number()
        self.app_data.remove_working_dictionary()
        self.app_data.set_working_dictionary()
        self.set_new_words()
        self.update_main_ui()

    def exit_button_clicked(self):
        self.app_data.save_words_to_learn()
        self.close_application()

    def reset_lesson_button_clicked(self):
        self.app_data.remove_working_dictionary()
        self.app_data.set_working_dictionary()
        self.set_new_words()
        self.update_main_ui()

    def update_word_label(self, text):
        self.sm.get_screen("main").ids.label_word.text = text

    def update_language_label(self, text):
        self.sm.get_screen("main").ids.label_language.text = text

    def set_new_words(self):
        self.app_data.set_current_words()
        self.set_words(self.app_data.current_words)

    def change_image(self, image_path):
        self.sm.get_screen("main").image_source = image_path

    def change_label_word_font_color(self, color):
        self.sm.get_screen("main").ids.label_word.color = color


    @staticmethod
    def close_application():
        App.get_running_app().stop()