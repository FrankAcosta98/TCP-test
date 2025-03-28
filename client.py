import socket

HOST = '127.0.0.1'
PORT = 5000


def connect_to_server(host: str, port: int) -> socket.socket:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server: {host}:{port}")
    return client_socket


def handle_server_communication(client_socket: socket.socket) -> None:
    try:
        while True:
            message = input("Input: ").strip()
            client_socket.sendall(message.encode())

            if message.upper() == "DESCONEXION":
                print("Disconnecting from server.")
                break

            data = client_socket.recv(1024).decode()
            print(f"Server -> {data}")
    finally:
        client_socket.close()


def start_client() -> None:
    client_socket = connect_to_server(HOST, PORT)
    handle_server_communication(client_socket)


if __name__ == "__main__":
    start_client()
