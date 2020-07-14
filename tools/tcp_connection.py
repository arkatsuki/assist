from socket import *

if __name__ == "__main__":
    HOST = '192.168.246.129'  # or 'localhost'
    PORT = 3690
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    print('end')

    pass







