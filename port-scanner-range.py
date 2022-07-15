import socket

sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

# enter ip address
host = input("Enter the IPv4 address here: ")

# function to test if port of host is closed or open
def portscanner(port):
    if sock.connect_ex((host,port)):
        print("Port %d is closed" % (port))
    else:
        print("Port %d is open" % (port))

# test ports in a range 1-300
for port in range(1, 300):
    portscanner(port)