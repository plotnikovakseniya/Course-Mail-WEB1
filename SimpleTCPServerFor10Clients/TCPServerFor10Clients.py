import socket 
from threading import Thread

def processClient():
  while True:
    conn, addr = s.accept()                                                        
    while True:                                                                    
      data = conn.recv(1024)
      print(data)                                    
      if data==b'close': break                                        
      conn.send(data)                                                
    conn.close()
                                                     
s = socket.socket()                                                            
s.bind(('0.0.0.0', 2222))                                                              
s.listen(10)                                                                    
for i in range(10):
  newThread = Thread(target=processClient)
  newThread.start()
