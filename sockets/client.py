import socket

ADDRESS = ("localhost", 5050)

if __name__ == "__main__":
    with socket.socket() as client:
        client.connect(ADDRESS)

        while 1:
            client.send(input("→ ").encode())
            data = client.recv(4096).decode()
            if data:
                print(data)
            else:
                break
