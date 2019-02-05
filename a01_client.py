import socket
import a01_func

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(("localhost", 8888))

data = ("A"*2000).encode()

a01_func.send_data(s, data)

answer = a01_func.recv_data(s)
print(answer)
s.close()
