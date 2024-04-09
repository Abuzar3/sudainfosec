import socket

def scan_ports(host, port_range):
  """
  This function scans a range of ports on a given host and prints the open ports.

  Args:
    host: The hostname or IP address of the host to scan.
    port_range: A range of ports to scan, in the format "start-end".

  Returns:
    A list of open ports.
  """

  open_ports = []
  for port in range(port_range[0], port_range[1] + 1):
    try:
      # Create a socket object.
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      
      # Connect to the port.
      sock.connect((host, port))
      
      # Add the port to the list of open ports.
      open_ports.append(port)
      
      # Close the socket.
      sock.close()
    except Exception:
      pass

  return open_ports

# Get the host and port range from the user.
host = input("Enter the hostname or IP address of the host to scan: ")
port_range = input("Enter the range of ports to scan (start-end): ").split("-")

# Scan the ports and print the open ports.
open_ports = scan_ports(host, [int(port) for port in port_range])
print("The following ports are open on {}: {}".format(host, ",".join(map(str, open_ports))))
