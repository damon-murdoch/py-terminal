## Builtin Imports

# Python socket library
import socket

# Python struct library
import struct

# Python time library
import time

# Python system library
import sys

## Local Imports

# Configuration file
import config

def wait_multicast(sock):

    # Number of bytes to recv
    RECV = 1024

    # List of responses
    messages = []

    # Program is running
    running = True

    # While program is running
    while(running):

        print("Waiting ...")

        # Get bytes, address from broadcast
        data, addr = sock.recvfrom(RECV)

        print("Recieved %s bytes from %s ..." % (len(data), addr))

        messages.append([data, addr])

    # Receive/respond loop
    # while True:

    # print(sys.stderr, '\nwaiting to receive message')
    # data, address = sock.recvfrom(1024)
    
    # print(sys.stderr, 'received %s bytes from %s' % (len(data), address))
    # print(sys.stderr, data)

    # print(sys.stderr, 'sending acknowledgement to', address)
    # sock.sendto('ack', address)

# Main loop
def main():

    # Multicast group
    group = config.ADDR

    # Address to recieve on
    address = ('', config.PORT)

    # Create the udp socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the udp socket to the address
    sock.bind(address)

    # Tell the operating system to add the socket 
    # to the multicast group on all interfaces.
    group = socket.inet_aton(group)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    # Wait for the multicast messages
    wait_multicast(sock)

# If we are running the file directly
if __name__ == '__main__':

  print("Terminal Client Started!")

  print("Scanning on port " + str(config.PORT) + ' ...')

  print("Press Ctrl + C to exit.")

  # Call the main function
  main()