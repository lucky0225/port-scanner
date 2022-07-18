from ipaddress import ip_address
from socket import *
import optparse
from threading import *

# scanner with which specific ip addresses and ports can be tested

# run via cmd: python advanced-scanner.py -H "insert ipaddress" -p "insert port(s)"
# python advanced-scanner.py -H 192.168.0.1 -p 100,101,102

# error: "-H" und "-p" für cmd
# -H = IP Address or link/name (s. "portScan") 
# -H = ip_address(192.168.0.1)
# -p = 100,200,300,400,443,444

#test if ports of host are open or closed
def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print("[+]%d/tcp Open" % tgtPort)
    except:
        print("[-] %d/tcp Closed" % tgtPort)
    finally:
        sock.close()
    
# definition of host -> host can be IP or link/name
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("Unknown Host %s " %tgtHost)
    try:
        tgtName = gethostbyaddr(tgtIP)
        print("[+] Scan Results for: " + tgtName[0])
    except:
        print("[+] Scan Results for: " + tgtIP)
    setdefaulttimeout(1)
    # using threading to test several ports
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

# make it work for the command line
def main():
    parser = optparse.OptionParser("Usage of program: " + "-H <target host> -p <target port>")
    parser.add_option("-H", dest="tgtHost", type="string", help="specify target host")
    parser.add_option("-p", dest="tgtPort", type="string", help="specify target port seperated by comma")
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(",")
    if (tgtHost == None) or (tgtPorts[0] == None):
        print (parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == "__main__":
    print(main())
