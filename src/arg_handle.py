import argparse, os

class InvalidState(Exception):
  pass

class File:
  def __init__(self, path):
    self.path = path

  @property
  def last(self):
    return os.path.basename(os.path.normpath(self.path))

  @property
  def ext(self):
    _, ext = os.path.splitext(self.last)
    return ext

def handle(func):
  def wrap(*args, **kwargs):
    args = func(*args, **kwargs)

    if File(args.file).ext != '.py':
      raise InvalidState("You must pass in a python file using the `--file` option.")

    return args
  return wrap

@handle
def cli():
  parser = argparse.ArgumentParser()
  parser.add_argument('--file', '-f', help='Input file.', required=True)
  return parser.parse_args()

def main(args):
  print(args.file)

if __name__ == '__main__':
  try:
    main(cli())
  except (Exception, InvalidState) as error:
    print(error)
