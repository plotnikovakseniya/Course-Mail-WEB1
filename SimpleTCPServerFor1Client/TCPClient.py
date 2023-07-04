from time import sleep
import socket
req = "Hello tcp!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('0.0.0.0', 2222))
s.send(req)
rsp = s.recv(1024)
print(rsp)
sleep(10)
req = "one more time"
s.send(req)
rsp = s.recv(1024)
print(rsp)
req = "close"
s.send(req)
rsp = s.recv(1024)
print(rsp)
s.close()
