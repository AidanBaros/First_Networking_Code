import socket

HOST = "10.17.68.60"# my IP 10.17.68.59
PORT = 42069

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello World")
    data = s.recv(1024)

print(f"Received {data!r}")