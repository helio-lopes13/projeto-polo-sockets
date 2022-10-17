import socket


def server_process():
    """Processes the server's routine when a connection is accepted.

    It should be called after the server's setup and inside an infinite loop
    for the server to listen until it's turned off manually.
    """
    socket_connection, address = server.accept()

    path_file = socket_connection.recv(4096).decode()
    file_name = path_file.split('\\')[-1]

    print(f'Nome do arquivo: {file_name}')

    with open(f'server/uploads/{file_name}', 'wb') as file:
        while True:
            received_bytes = socket_connection.recv(4096)
            if not received_bytes:
                break
            file.write(received_bytes)

    socket_connection.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 30000))
server.listen(5)
print('Servidor rodando...')


def run():
    """Executes the code"""
    while True:
        server_process()
