import sys, socket, os
from enum import Enum
from cli import cli

class Config:
  SERVER_HOST = '0.0.0.0'
  SERVER_PORT = 8000
  FILES = '../doc'

class Status(Enum):
  OK = 1
  NOT_FOUND = 2
  SERVER_ERROR = 3

  def __str__(self):
    return {
        Status.OK: 'HTTP/1.0 200 OK\n\n',
        Status.NOT_FOUND: 'HTTP/1.0 404 NOT FOUND\n\n',
        Status.SERVER_ERROR: 'HTTP/1.0 500 INTERNAL SERVER ERROR\n\n'
    }[self]

class Message:
  def __init__(self, headers):
    self.headers = headers.split("\n")

  @property
  def method(self):
    return self.headers[0].split()[0]

  @property
  def path(self):
    path = self.headers[0].split()[1]
    if path == "/":
      path = "index.html"
    return path

  @property
  def version(self):
    return self.headers[0].split()[2]

  @property
  def as_dict(self):
    d = {}

    for header in self.headers:
      curr = header.split(':')
      if len(curr) < 2:
        continue
      d[curr[0]] = curr[1]

    return {**{'method': self.method, 'path': self.path, 'version': self.version}, **d}

class Socket:
  def __init__(self, host, port):
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.socket.bind((host, port))

  def listen(self):
    self.socket.listen(1)

  def accept(self):
    return self.socket.accept()

def handle(message):
  file = os.path.join(Config.FILES, message.path)

  if not os.path.exists(file):
    return (Status.NOT_FOUND, None)

  with open(file, 'r') as f:
    content = f.read()

  return (Status.OK, content)

def main(args):
  host, port = (args.hostname or Config.SERVER_HOST, args.port or Config.SERVER_PORT)

  sock = Socket(host, port)
  sock.listen()
  print(f'Listening on port: {port}')

  while True:
    print('Waiting for a connection.')
    conn, client_addr = sock.accept()

    req = conn.recv(1024).decode()
    print(f'Received request from client: {req}')

    status, data = handle(Message(req))
    conn.sendall((str(status) + data if data else "").encode())
    conn.close()

  sock.close()

if __name__ == '__main__':
  main(cli())
