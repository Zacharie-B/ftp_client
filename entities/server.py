# Interface for server interaction
from abc import ABC, abstractmethod


class Server(ABC):
    @property
    @abstractmethod
    def port_number(self):
        pass
