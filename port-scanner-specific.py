import socket


# socket.AF_INET      - stance for IPv4
# socket.SOCK_STREAM  - stance for tcp packets
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# print "closed" if 2 seconds expire without a result
socket.setdefaulttimeout(2)

# insert IPv4 address
# IPv4 -> "ipconfig" in cmd
#insert IPv4 address
host = input("Insert the IPv4 address here: ")

#example port (e.g. 443)
port = int(input("Insert the port here: "))

# function to test, if port is open
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
