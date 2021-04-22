import socket
class TCPClient:
    def request(self):
        print('==== request start ====')
        try:
            client_socket = socket.socket()
            client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            print('==== connecting server ====')
            client_socket.connect(("localhost", 8000))
            print('==== connection end ====')
            with open('client_send.txt','rb') as f:
                reqest = f.read()
            client_socket.send(reqest)
            responce = client_socket.recv(4096)
            with open('client_recv.txt','wb') as f:
                f.write(responce)
        finally:
            client_socket.close()
            print('==== end ====')


if __name__ == '__main__':
    client = TCPClient()
    client.request()
