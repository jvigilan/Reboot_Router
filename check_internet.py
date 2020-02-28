import socket

def is_connected(hostname):
  """
  Quick check for internet connectivity using sockets
  :param hostname: website to try and connect to
  :return: true or false
  """
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(hostname)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except:
     pass
  return False

#print(is_connected(REMOTE_SERVER))