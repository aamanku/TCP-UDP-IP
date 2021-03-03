# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:40:57 2020

@author: Aamanku
"""
#This code assumes all the packed data is of type double.


import socket
import struct

buffer_size=8#8 for double
data_type='d' #'d' for double
UDP_IP = '192.168.2.2'#host ip
UDP_PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    raw, addr = sock.recvfrom(10240)
    print(raw)
    # breakpoint()
    for i in range(0,int(len(raw)/buffer_size)):#data at 'buffer_size' bits interval
        # breakpoint()
        print(struct.unpack_from(data_type, raw,i*buffer_size)[0])

