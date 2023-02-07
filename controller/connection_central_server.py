import socket
from entities.central_server import CentralServer

"""Réalise la connexion entre notre client ftp et le serveur centralisé."""


class ConnectionCentralServer:
    def __init__(self, hostname, port, ip="127.0.0.1"):
        self.server = CentralServer(hostname, port, ip)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.server.get_ip_address(),
                        self.server.get_port_number()))

    # Envoi un message au serveur centralisé
    def send_msg(self, msg):
        if msg == "exit":
            self.s.close()
        msg = bytes(msg, 'utf-8')
        print(msg)
        self.s.send(msg)
        data = self.s.recv(2000)
        print("Client reçoit :", data.decode('utf-8'))

