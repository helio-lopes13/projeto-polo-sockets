import socket


def client_function(host: str, port: int):
    """Creates a client socket to connect with the server and executes the client's routine.

    Args:
        host: the IP address where the server socket is located
        port: the port utilized in the server machine for the connection
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((host, port))

    file_path = str(input('Caminho do arquivo > '))

    client.send(file_path.encode())

    with open(file_path, 'rb') as file:
        while True:
            read_bytes = file.read(4096)
            if not read_bytes:
                break
            client.send(read_bytes)
        print('\nEnvio do arquivo concluído!')


client_function('localhost', 30000)
