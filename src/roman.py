import argparse
from unittest import TestCase

A = {
  1000: 'M',
  900: 'CM',
  500: 'D',
  400: 'CD',
  100: 'C',
  90: 'XC',
  50: 'L',
  40: 'XL',
  10: 'X',
  9: 'IX',
  5: 'V',
  4: 'IV',
  1: 'I'
}

B = {
  'M': 1000,
  'CM': 900,
  'D': 500,
  'CD': 400,
  'C': 100,
  'XC': 90,
  'L': 50,
  'XL': 40,
  'X': 10,
  'IX': 9,
  'V': 5,
  'IV': 4,
  'I': 1
}

def serialize(v: int) -> str:
  ret = ''
  for key in A:
    rem = v % key
    if v // key > 0:
      ret += (v // key) * A[key]
    v = rem
  return ret

def deserialize(v: str) -> int:
  i = 0
  tokens = []
  while i < len(v):
    if i + 1 < len(v):
      t = v[i] + v[i + 1]
      if t in ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']:
        tokens.append(t)
        i += 2
        continue
    tokens.append(v[i])
    i += 1
  return sum(list(map(lambda token: B[token], tokens)))

def cli():
  parser = argparse.ArgumentParser()

  parser.add_argument(
    '--to', '-t', action='store_true', help='Roman numeral to integer.'
  )

  return parser.parse_args()

def main(args):
  print(
    (lambda v: serialize(int(v)), lambda v: deserialize(v))[args.to](input())
  )

if __name__ == '__main__':
  try:
    main(cli())
  except Exception as error:
    print(str(error))

class SerializeTestCase(TestCase):
  def setUp(self):
    self.cases = [(3, 'III'), (58, 'LVIII'), (1994, 'MCMXCIV')]

  def test_serialize(self):
    for have, want in self.cases:
      assert serialize(have) == want

class DeserializeTestCase(TestCase):
  def setUp(self):
    self.cases = [('III', 3), ('LVIII', 58), ('MCMXCIV', 1994)]

  def test_deserialize(self):
    for have, want in self.cases:
      assert deserialize(have) == want
