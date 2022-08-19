# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from ssdpy import SSDPServer
import os
import socket

bind = os.getenv("BIND_ADDRESS", "0.0.0.0")

server = SSDPServer(usn="rpi:remotewaker:" + socket.gethostname(), address=bind, device_type="ssdp:remotewaker", location="http://" + bind + "/setup")


server.serve_forever()
