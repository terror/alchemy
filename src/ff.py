import ast, collections, argparse, os

class File:
  def __init__(self, path):
    self.path = path

  @property
  def last(self):
    return os.path.normpath(os.path.basename(self.path))

  @property
  def ext(self):
    _, ext = os.path.splitext(self.last)
    return ext

class Visitor(ast.NodeVisitor):
  def __init__(self, counter):
    self.counter = counter

  def visit_Call(self, node):
    if isinstance(node.func, ast.Name):
      self.counter[node.func.id] += 1

def cli():
  parser = argparse.ArgumentParser()
  parser.add_argument("--file", "-f", help="Python file.")
  return parser.parse_args()

def main(args):
  if not args.file:
    print("You must provide a valid python file.")
    return

  file = File(args.file)

  if file.ext != ".py":
    raise Exception("File must be a valid python file.")

  with open(File(args.file).path) as file:
    tree = ast.parse(file.read())

  visitor = Visitor(collections.Counter())
  visitor.visit(tree)

  for name, count in visitor.counter.items():
    print(name, count)

if __name__ == '__main__':
  try:
    main(cli())
  except Exception as error:
    print(error)
