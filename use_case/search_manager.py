# Manage the use of search which commanded by user


from entities.result_search import ResultSearch
from use_case.searching import Searching
from use_case.searching_files import SearchingFiles


class SearchManager:
    def __init__(self):
        self.request = Searching()
        self.results_search = list()
        self.searching_files = SearchingFiles()

    def request_search(self, keywords: list[str], ip_address: str):
        key_words = self.request.make_request(keywords)

        result = self.searching_files.searching_files(keywords)

        print(result)





