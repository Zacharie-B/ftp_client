# Store the search already done to reuse this search if necessary


class SearchCache:
    def __init__(self, searches):
        self.searches = searches

    def add(self, search):
        self.searches.append(search)

    def remove_all(self):
        self.searches.clear()

    def get_searches(self):
        return self.searches
