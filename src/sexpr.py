import argparse
import ast
import string
import sys
import unittest
from collections import deque

# **** tests ****

class TestParse(unittest.TestCase):
  def setUp(self):
    self.cases = [
      ('(first (list 1 (+ 2 3) 9))',            ['first', ['list', 1, ['+', 2, 3], 9]]),
      ('(first (list 1 (+ 2 3.5) 9.4))',        ['first', ['list', 1, ['+', 2, 3.5], 9.4]]),
      ('(+ 3 (* 5 4 (/ 7 8)))',                 ['+', 3, ['*', 5, 4, ['/', 7, 8]]]),
      ('(+ 322 (* 55 488 (/ 78 81)))',          ['+', 322, ['*', 55, 488, ['/', 78, 81]]]),
      ('(+ 1 (+ 2 3 (+ 4 5 (+ 6 7 (+ 8 9)))))', ['+', 1, ['+', 2, 3, ['+', 4, 5, ['+', 6, 7, ['+', 8, 9]]]]]),
      ('()',                                    [])
    ]

  def test_parse(self):
    for expr, result in self.cases:
      self.assertEqual(parse(expr), result)

class TestEval(unittest.TestCase):
  def setUp(self):
    self.cases = [
      ('(+ 1 2)', 3),
      ('(+ 1 2 (* 3 4 (+ 1 1)))', 27)
    ]

  def test_eval(self):
    for expr, result in self.cases:
      self.assertEqual(eval(expr), self.cases)

# **** core ****

def eval(tokens):
  # evaluate each sub expression
  # ['+', 1, 2 ['+', 3, 4]]
  # -> ['+', 1, 2, 7]
  # -> [10]
  # -> 10
  pass

def eval_scalar(s):
  try:
    s = ast.literal_eval(s)
  except:
    pass
  return s

def parse(expr):
  # str | number -> append to current list
  # (            -> append a list
  # )            -> merge current list with previous
  # ['+', ' ', '3', ' ', '(', '*', ' ', '5', ' ', '4', ' ', '(', '/', ' ', '7', ' ', '8', ')', ')']
  expr   = deque(expr[1:][:-1])
  result = [[]]
  while expr:
    curr = expr.popleft()
    if curr == '(':
      result.append([])
    elif curr == ')':
      result[-2].append(result.pop())
    else:
      if curr == ' ':
        continue
      while expr[0] not in ['(', ')', ' ']:
        curr += expr.popleft()
      result[-1].append(eval_scalar(curr))
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
  print(parse(('(+ 3 (* 5 4 (/ 7 8)))')))

if __name__ == '__main__':
  main(cli())
