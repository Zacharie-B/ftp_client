# Interface for server interaction
from abc import ABC, abstractmethod


class Server(ABC):
    @abstractmethod
    def get_port_number(self):
        pass

    @abstractmethod
    def get_ip_address(self):
        pass
