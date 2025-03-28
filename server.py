import socket

HOST = '127.0.0.1'
PORT = 5000


def create_server_socket(host: str, port: int) -> socket.socket:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server listening on: {host}:{port}")
    return server_socket


def handle_client_connection(client_socket: socket.socket, client_address: tuple) -> None:
    print(f"Connected to client: {client_address}")

    while True:
        data = client_socket.recv(1024).decode()

        if not data:
            break

        print(f"Client {client_address} -> {data}")

        if data.strip().upper() == "DESCONEXION":
            print(f"Client {client_address} disconnected.")
            break

        response = data.upper()
        client_socket.sendall(response.encode())

    client_socket.close()


def start_server() -> None:
    server_socket = create_server_socket(HOST, PORT)

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            handle_client_connection(client_socket, client_address)
    except KeyboardInterrupt:
        print("\nServer shutting down.")
    finally:
        server_socket.close()


if __name__ == "__main__":
    start_server()
