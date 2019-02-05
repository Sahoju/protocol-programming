import sys
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

def send_data(socket, data):
	total = 0
	print("sys.getsizeof(data): " + str(sys.getsizeof(data)))
	data_len = sys.getsizeof(data)
	print("send_data data_len: " + str(data_len) + ", type: " + str(type(data_len)))

	while total < data_len:
		sent = socket.send(data[total:])
		print("send_data sent: " + str(sent) + ", type: " + str(type(sent)))
		if sent == 0:
			raise RuntimeError("socket connection broken")
		total += sent
		print("send_data total: " + str(total) + ", type: " + str(type(total)))

def get_data_length(socket):
	buffest = "".encode()
	while True:
		hlep = socket.recv(1)
		print("get_data_length hlep:" + str(hlep))
		if hlep == b'':
			break
		buffest += hlep
	return int(len(buffest.decode()))

def recv_data(socket):
	received = 0
	chunks = []
	length = get_data_length(socket)
	while received < length:
		chunk = socket.recv(min(length - received, 2048))
		chunks.append(chunk)
		received += sys.getsizeof(chunk)
	print("received " + str(received) + " bytes")
		


