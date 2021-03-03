# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:02:32 2020

@author: amkulk
"""

import socket
import struct
import time
buffer_size=8 #for double
UDP_IP = '192.168.2.2'#host ip
UDP_PORT = 3333

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
num=0

old_time=time.time()
data=struct.pack('d',8008135)
sock.sendto(data,('192.168.2.2',6969))
