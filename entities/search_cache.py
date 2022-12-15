# Store the search already done to reuse this search if necessary


class SearchCache:
    def __init__(self):
        self.__searches = list()

    def add(self, search):
        self.__searches.insert(0, search)

    def remove_all(self):
        self.__searches.clear()

    def get_searches(self):
        return self.__searches

    def __str__(self):
        string = "Your previous searches are :"
        for search in self.__searches:
            string += "\n"
            keywords = search.get_key_words()
            for k in keywords:
                string += k + " "
        return string
