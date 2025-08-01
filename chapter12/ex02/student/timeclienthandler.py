"""
File: timeclienthandler.py
Programming Exercise 12.2

Client handler for providing the day and time.
"""

from time import ctime
from threading import Thread
from codecs import decode

class TimeClientHandler(Thread):
    """Handles a client request."""
    def __init__(self, client):
        Thread.__init__(self)
        self.client = client
   
    def run(self):
        self.client.send(bytes(ctime() + \
                               "\nHave a nice day!",
                               "ascii"))
        self.client.close()

import socket
import sys

def main():
    host = 'localhost'
    port = 12345

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))

        data = sock.recv(1024)
        print(data.decode())
        sock.close()
        print("Have a nice day!")

    except ConnectionRefusedError:
        print("Error connecting to the server")
        sys.exit(1)

if __name__ == "__main__":
    main()

