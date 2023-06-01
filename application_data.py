import os
import random

class ApplicationData():
    CONGRATULATIONS = " Glückwunsch! \nKein Wort übrig, Congratulations!\n    No word left  , Gratulacje! \n Nie zostało żadne słowo"
    NUMBER_OF_WORDS_LOADED = 100
    dictionary_file = "resources/data/german_words.csv"
    working_dictionary_file = os.path.expanduser("~/Documents/german_words_to_learn.csv")


    def __init__(self):
        self.dictionary = self.load_dictionary()
        self.set_word_package_number()
        self.working_dictionary = self.load_working_dictionary()
        self.set_current_words()
        self.word_count = len(self.working_dictionary)

    def load_csv_file(self, file):
        with open(file, "r") as csv_file:
            return csv_file.readlines()


    def load_dictionary(self):
        return self.load_csv_file(self.dictionary_file)


    def load_working_dictionary(self):
        if os.path.exists(self.working_dictionary_file):
            return self.load_csv_file(self.working_dictionary_file)
        else:
            return self.get_package_from_dictionary()


    def set_working_dictionary(self):
        self.working_dictionary = self.load_working_dictionary()


    def set_word_package_number(self):
        self.word_package_number = random.randint(1, round(len(self.dictionary)/100))


    def get_package_from_dictionary(self):
        work_dict = []
        for i, line in enumerate(self.dictionary):
            if self.NUMBER_OF_WORDS_LOADED * (self.word_package_number - 1) <= i < self.NUMBER_OF_WORDS_LOADED * self.word_package_number:
                work_dict.append(line)
        return work_dict


    def pick_random_word(self):
        return random.choice(self.working_dictionary)


    def set_current_words(self):
        if len(self.working_dictionary) > 0:
            self.current_words = self.pick_random_word()
        else:
            self.current_words = self.CONGRATULATIONS


    def remove_current_word_from_dictionary(self):
        if len(self.working_dictionary) > 0:
            self.working_dictionary.remove(self.current_words)


    def save_words_to_learn(self):
        file_path = os.path.expanduser("~/Documents/german_words_to_learn.csv")
        with open(file_path, "w") as data_file:
            for words in self.working_dictionary:
                data_file.write(words)


    def remove_working_dictionary(self):
        if os.path.exists(os.path.expanduser("~/Documents/german_words_to_learn.csv")):
            os.remove(os.path.expanduser("~/Documents/german_words_to_learn.csv"))