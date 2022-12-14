# Store the location and the search files of one ftp server


class ResultSearch:
    def __init__(self, location: str, files_name: list[str]):
        self.__location = location
        self.__files_name = files_name

    def get_location(self):
        return self.__location

    def get_files_name(self):
        return self.__files_name

    def __str__(self):
        string = "The files searched on " + self.__location + " are named :"
        for file_name in self.__files_name:
            string.__add__(" ")
            string.__add__(file_name)
        return string
