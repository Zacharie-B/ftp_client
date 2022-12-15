# Describe information to access at central server
from entities.server import Server
from entities.local_server import LocalServer


class CentralServer(Server):
    port_number = -1

    def __init__(self, hostname: str, ip_address: str, port_number: int):
        self.__hostname = hostname
        self.__ip_address = ip_address
        self.port_number = port_number

    def get_number_port(self):
        return self.port_number

    def get_hostname(self):
        return self.__hostname

    def get_ip_address(self):
        return self.__ip_address


cs = CentralServer('abc', '1.1.1.1', 3470)
print(cs.get_hostname())
print(cs.get_ip_address())
print(cs.get_number_port())

ls = LocalServer(5578)
print(ls.get_number_port())
print(cs.get_number_port())

