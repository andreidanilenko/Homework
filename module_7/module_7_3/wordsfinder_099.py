import re

class WordsFinder:
    def __init__(self, *file_names: str):
        self.file_names = file_names
        self.all_words = self.get_all_words()

    def get_all_words(self):
        all_words = {}
        for f in self.file_names:
            with open(f, encoding='utf-8') as file:
                content = file.read().lower()
                words = re.findall(r'\b\w+\b', content)
                all_words[f] = words
        return all_words

    def find(self, word):
        result_dict = {}
        word = word.lower()
        for filename, words in self.all_words.items():
            if word in words:
                result_dict[filename] = words.index(word) + 1
        return result_dict

    def count(self, word):
        result_dict = {}
        word = word.lower()
        for filename, words in self.all_words.items():
            count = words.count(word)
            if count > 0:
                result_dict[filename] = count
        return result_dict