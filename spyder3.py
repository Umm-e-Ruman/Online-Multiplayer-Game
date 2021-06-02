import socket

class Network:
    def  init (self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.106"
        self.port = 5555
        self.addr = (self.server)
        self.pos = self.connect()
        
    def getPos(self):
         return self.pos
        
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
    def send(self, data):
        try:
            self.client.recv(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
