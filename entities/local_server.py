# Do interactions with local server
from entities.server import Server


class LocalServer(Server):
    port_number = -1

    def __init__(self, port_number):
        self.port_number = port_number

    def get_number_port(self):
        return self.port_number

    def add_file_in_list(self):
        pass
