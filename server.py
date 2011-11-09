import socket
import threading

class Server():
    def __init__(self, port = 6886):
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = port
        self.timeToStop = False
        self.clients = []
        self.run()

    def run(self):
        self.tcpsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpsoc.bind((self.host, self.port))
        self.tcpsoc.listen(5)
        while self.timeToStop == False:
            self.conn, self.addr = self.tcpsoc.accept()
            self.clients.append(Client(self.conn))

class Client(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connection = conn
        self.connection.send(b'oh hey there :)')

def main():
    server = Server()

if __name__ == '__main__':
    main()