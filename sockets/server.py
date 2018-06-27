import socket
import threading

ADDRESS = ("localhost", 5050)


def handler(sock, address):
    print("Client connected at %s:%i" % address)

    with sock:
        data = sock.recv(4096)
        while data:
            sock.send(data)
            data = sock.recv(4096)


if __name__ == "__main__":
    with socket.socket() as server:
        server.bind(ADDRESS)
        server.listen()
        print("Server running on %s:%i" % ADDRESS)

        while 1:
            conn = server.accept()
            threading.Thread(target=handler, args=conn).start()
