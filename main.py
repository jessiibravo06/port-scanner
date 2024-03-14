#======= Simple port Scanner ========
import socket

#captures ipv4 adress and port number to scan
target = input("Enter IP address: ")
port = input("Enter port: ")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def portScanner(port):
    if s.connect_ex(target, port):
        print("port is closed")
    else:
        print("port is open")

#calling function
portScanner(port)


