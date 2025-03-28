import socket

HOST = '127.0.0.1'
PORT = 5000


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server listening on: {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to client: {client_address}")

        handle_client(client_socket, client_address)


def handle_client(client_socket, client_address):
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


if __name__ == "__main__":
    start_server()
