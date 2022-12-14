# Store keywords use during the search.


class Search:
    def __init__(self, key_words: list[str]):
        self.__key_words = key_words

    def get_key_words(self):
        return self.__key_words
