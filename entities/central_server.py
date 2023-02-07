# Describe information to access at central server
from abc import ABC

from entities.server import Server
from entities.local_server import LocalServer


class CentralServer(Server):

    def __init__(self, hostname: str, port_number: int, ip_address="127.0.0.1"):
        self.__hostname = hostname
        self.__ip_address = ip_address
        self.port_number = port_number

    def get_hostname(self):
        return self.__hostname

    def get_port_number(self):
        return self.port_number

    def get_ip_address(self):
        return self.__ip_address



