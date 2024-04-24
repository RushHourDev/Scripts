#Script to perform a simple banner grab using the "socket" module
#Example use: BannerGrab.py www.google.com 80

#Import modules
import socket
import sys

#Init variables from arguments[1] and [2]
#Needed to cast second argument from str to int
url = sys.argv[1]
port = int(sys.argv[2])

#Function to grab banner
def banner_grab(url, port):
  try:
    #setting default socket timeout so connection doesn't hang forever
    socket.setdefaulttimeout(10)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((url,port))
    banner = s.recv(1024)
    print("[+] Banner: " + banner.decode().string())
    s.close()
  except Exception as e:
    print("[-] Error: " + str(e))

banner_grab(url, port)
