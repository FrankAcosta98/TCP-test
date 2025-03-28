import socket

HOST = '127.0.0.1'
PORT = 5000


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(f"Connected to server: {HOST}:{PORT}")

    try:
        communicate_with_server(client_socket)
    finally:
        client_socket.close()


def communicate_with_server(client_socket):
    while True:
        message = input("Input: ").strip()
        client_socket.sendall(message.encode())

        if message.upper() == "DESCONEXION":
            print("Disconnecting from server.")
            break

        data = client_socket.recv(1024).decode()
        print(f"Server -> {data}")


if __name__ == "__main__":
    start_client()
