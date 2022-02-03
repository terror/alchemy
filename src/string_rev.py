from typing import List

def A(s: str) -> str:
  ret = list(s)
  for i in range(len(s) // 2):
    ret[i], ret[~i] = ret[~i], ret[i]
  return ''.join(ret)

def B(s: str) -> str:
  ret = ''
  for i in range(len(s) - 1, -1, -1):
    ret += s[i]
  return ret

def C(s: str) -> str:
  if not len(s):
    return ''
  return s[-1] + C(s[:-1])

def D(s: str) -> str:
  return ''.join(reversed(list(s)))

def E(s: str) -> str:
  return s[::-1]

def F(s: str) -> str:
  ret = ''
  for char in s:
    ret = char + ret
  return ret

def G(s: str) -> str:
  ret = list(s)
  i, j = 0, len(ret) - 1
  while i < j:
    ret[i], ret[j] = ret[j], ret[i]
    i += 1
    j -= 1
  return ''.join(ret)

if __name__ == '__main__':
  cases = [('hello', 'olleh'), ('yo', 'oy'), ('abc123', '321cba')]
  for func in [A, B, C, D, E, F, G]:
    for have, want in cases:
      assert func(have) == want
