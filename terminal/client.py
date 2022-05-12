## Builtin Imports

# Python socket library
import socket
from tempfile import TemporaryFile

# Python time library
import time

## Local Imports

# Configuration file
import config

def wait(sock):

    # Sleep Timer (ms)
    SLEEP = 8 * 0.001

    # Byte limit
    RECV = 1024

    # Keep running unless fatal error
    running = True

    # Keep going until unset
    while running: 

        try:

            # Recieve the content from the socket
            message = sock.recvfrom(RECV)

            # Print the length of the recieved message
            print("Recieved:" + len(message))

        except TimeoutError as e: # Timeout exception

            print("Warning: Timed out")

        except Exception as e: # Other error

            print("Error: " + e)

            # Disable the running
            running = False

        finally: # Do after regardless of error

            # Sleep for 'SLEEP' milliseconds
            time.sleep(SLEEP)

# Main loop
def main():
    
    # Request Timeout
    TIMEOUT = 0.2

    # Address, port we are recieving data from
    group = ('0.0.0.0',  config.PORT)

    # Create the main socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Socket timeout
    sock.settimeout(TIMEOUT)

    # Bind to the multicast address
    sock.bind(group)

    print("Checking for messages ...")

    # Wait for requests on the socket
    wait(sock)

# If we are running the file directly
if __name__ == '__main__':

  print("Terminal Client Started!")

  print("Recieving on " + ", ".join(('0.0.0.0',  str(config.PORT))) + ' ...')

  print("Press Ctrl + C to exit.")

  # Call the main function
  main()