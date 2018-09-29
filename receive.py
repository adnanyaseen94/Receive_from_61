import socket
import sys
import struct
from tofloat import tofloat
import time
import numpy as np

def receive(IP, Port, NumData):

	# Create a UDP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# Bind the socket to the port
	server_address = (IP, Port)
	print('starting up on {} port {}'.format(*server_address))
	sock.bind(server_address)

	num_data_rcv = NumData
	num_data_rcv = int(num_data_rcv)
	out = np.zeros(num_data_rcv)

	print('\nwaiting to receive message')
	data, address = sock.recvfrom(8192)
	print('received {} bytes from {}'.format(len(data), address))
	for i in range(0, num_data_rcv):
#		print(tofloat(data[(4*i):(4+4*i)]))
		out[i] = tofloat(data[(4*i):(4+4*i)])
#	time.sleep(0.05)

	return out


