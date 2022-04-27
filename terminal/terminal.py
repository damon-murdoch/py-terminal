## Builtin Imports

# Python socket library
import socket

# Python struct library
import struct

# Python time library
import time

# Operating System Library
import os

## Local Imports

# Configuration file
import config

# Data file
import data

# spam_socket(sock: Socket, data: List, target: Tuple): Void
# Given a socket, starts an infinite loop sending the data
# on the given socket to the multi cast group provided.
def spam_multicast(sock, data, target): 

  # Sleep Timer (ms)
  SLEEP = 8 * 0.001

  # Infinite loop
  while(True):

    try:

      # Loop over all of the byte sequences
      for sequence in data:

        # Send all of the event mode 4P Sequences
        sock.sendto(bytes(sequence), target)

      # Sleep for 'SLEEP' milliseconds
      time.sleep(SLEEP)

    except TimeoutError as e: # Warning

      print("Timeout Warning: " + str(e))

    except Exception as e: # Critical

      # Pass to parent
      raise e

# Main loop
def main():

  # Request Timeout
  TIMEOUT = 0.2

  # Reuse Config
  REUSE = 1

  # Packet Time To Live (TTL)
  TTL = 255

  # No idea what the 10,000 is for, just a placeholder
  multicast_group = (config.ADDR,  config.PORT)

  # Create the udp socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  # Socket timeout
  sock.settimeout(TIMEOUT)

  # Set multicast time to live to the config setting
  # ttl = struct.pack('b', TTL)
  sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, TTL)

  # No idea what this is for, oops
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, REUSE) 
  sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, REUSE)

  try:

    # If free play mode is enabled
    if config.FREEPLAY:

      if config.EVENTMODE == 0: # Free Play

        # Spam the free play mode packets on the multicast port
        spam_multicast(sock, data.terminalPackage_Free, multicast_group)

      elif config.EVENTMODE == 1: # Event Mode 2P

          # Spam the event 2P mode packets on the multicast port
          spam_multicast(sock, data.terminalPackage_Event2P, multicast_group)            

      elif config.EVENTMODE == 2: # Event Mode 4P

          # Spam the event 4P mode packets on the multicast port
          spam_multicast(sock, data.terminalPackage_Event4P, multicast_group)
    
    else: # Free play mode is disabled

      # Spam the coin play mode packets on the multicast port
      spam_multicast(sock, data.terminalPackage_Coin, multicast_group)

  except Exception as e: # Server crash

    print("Server crashed: " + e)  

# If we are running the file directly
if __name__ == '__main__':

  print("Terminal Started!")

  print("Free Play: " + str(config.FREEPLAY))
  print("Event Mode: " + str([
    "Disabled", "2P MODE", "4P MODE"
  ][config.EVENTMODE]))

  print("Press Ctrl + C to exit.")

  # Call the main function
  main()