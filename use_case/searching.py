# Create the request to search files with keywords
# It save also keywords of this search

from entities.search import Search
from entities.search_cache import SearchCache


class Searching:
    def __init__(self):
        self.__search_cache = SearchCache()

    def make_request(self, keywords: list[str]):
        search = Search(keywords)

        request = ""
        for item in search.key_words:
            request += item + " "

        self.save_request(search)

        return request

    def save_request(self, search: Search):
        self.__search_cache.add(search)

    def get_search_cache(self):
        return self.__search_cache.get_searches()
