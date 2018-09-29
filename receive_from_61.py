#import socket
import sys
import struct
from tofloat import tofloat
import time
from send import send
from receive import receive
import numpy as np
import threading
import logging


IP_receive = '134.130.169.40'   # Ip where where data is being sent (from 61)
Port_receive_61 = 6060          # Port where data is being sent (from 61)

NumData = 12



def receiver_PI_61():
    timeout_receive = time.time()+1;
    logging.debug('Starting')
    while True:
        data_IP61 = receive(IP_receive,Port_receive_61,12)
        time.sleep(0.02)
        print("received = ", data_IP61)
        file = open("data_received_61.txt","w") 
        file.write(data_IP61) 
        file.close()
        
        




w = threading.Thread(name='receiver_PI_61', target=receiver_PI_61)

w.start()


