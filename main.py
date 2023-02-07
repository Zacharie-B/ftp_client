import controller.connection_central_server as co

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    connection_central_server = co.ConnectionCentralServer("SRV01", 9999)

    while 1:
        msg = input("Client: Entrez un message ou exit pour sortir:")
        connection_central_server.send_msg(msg)
