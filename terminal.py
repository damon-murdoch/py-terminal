# Python socket library
import socket

# Python struct library
import struct

# Python system library
import sys

# Configuration file
import config

# Main loop
def main():

  # No idea what the 10,000 is for, just a placeholder
  multicast_group = (config.MULTICAST_ADDR,  config.PORT)

  # Create the udp socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  # Socket timeout
  sock.settimeout(config.TIMEOUT)

  # Set multicast time to live to the config setting
  ttl = struct.pack('b', config.TTL)
  sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

  # No idea what this is for, oops
  reuse = struct.pack('b', 1)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, reuse) 
  sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, reuse)

  # Server is running
  running = True

  try:

    # If free play mode is enabled
    if config.FREEPLAY:

      # Switch on event mode value
      match config.EVENTMODE: 

        case 0: # No event mode

          pass

        case 1: # Event Mode 2P

          pass

        case 2: # Event Mode 4P

          pass

    # sent = sock.sendto("", multicast_group)

  except:
    
    pass

  finally:

    pass

# If we are running the file directly
if __name__ == '__main__':

  # Call the main function
  main()