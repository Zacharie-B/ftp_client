# Store the search already done to reuse this search if necessary

from entities.search import Search


class SearchCache:
    def __init__(self):
        self.__searches = list[Search]

    def add(self, search):
        self.__searches.insert(0, search)

    def remove_all(self):
        self.__searches.clear()

    def get_searches(self):
        return self.__searches

    def __str__(self):
        string = "Your previous searches are :"
        for search in self.__searches:
            string.__add__("\n")
            string.__add__(search)
        return string
