import sys, argparse, unittest, ast
from collections import deque

# **** tests ****

class TestParse(unittest.TestCase):
  def setUp(self):
    self.cases = [('(first (list 1 (+ 2 3) 9))', ["first", ["list", 1, ["+", 2, 3], 9]]),
                  ('(first (list 1 (+ 2 3.5) 9.4))', ["first", ["list", 1, ["+", 2, 3.5], 9.4]])]

  def test_parse(self):
    for expr, result in self.cases:
      self.assertEqual(parse(expr), result)

# **** core ****

def eval(s):
  try:
    s = ast.literal_eval(s)
  except:
    pass
  return s

def parse(expr):
  # str | number -> append to current list
  # (            -> append a list
  # )            -> merge current list with previous
  # ['first', '(list', '1', '(+', '2', '3)', '9)']
  expr = deque(expr[1:][:-1].split())
  result = [[]]
  while expr:
    curr = expr.popleft()
    first, last = curr[0], curr[-1]
    if first == '(':
      result.append([curr[1:]])
    elif last == ')':
      result[-1].append(eval(curr[:-1]))
      result[-2].append(result.pop())
    else:
      result[-1].append(eval(curr))
  return result[0]

def cli():
  parser = argparse.ArgumentParser()
  parser.add_argument('--test', '-t', action='store_true')
  return parser.parse_args()

def main(args):
  if args.test:
    sys.argv = [sys.argv[0]]
    unittest.main()
    return
  print(parse('(first (list 1 (+ 2 3) 9))'))

if __name__ == '__main__':
  main(cli())
