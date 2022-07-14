import socket


# socket.AF_INET      - stance for IPv4
# socket.SOCK_STREAM  - stance for tcp packets

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#insert IPv4 address
ip_1 = ""
host = ip_1

#example port
port = 443

#function to test, if port is open
def portscanner(port):
    #if connection results in error -> closed
    if sock.connect_ex((host,port)):
        print("Port %d is closed" % (port))
    #else -> open
    else:
        print("Port %d is opened" % (port))

print(portscanner(port))


"""
ip_1 = ""

def test():
    if ip_1 == str:
        ip = ip_1
        print(ip)
    else:
        ip = input("Insert IPv4 here: ")
        print(ip)

print(test())

host = ip_1
"""