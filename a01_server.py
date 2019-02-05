import socket
import a01_func

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("localhost", 8888))
s.listen(5)

client, addr = s.accept()
message = a01_func.recv_data(client)
print(message)

a01_func.send_data(client, "received".encode())
client.close()
s.close()
