import time, functools

class Foo:
  def __init__(self, n = 1):
    self.n = n

  @functools.cached_property
  def expensive(self):
    return fib(self.n)

class Mark:
  def __init__(self):
    self.time = time.perf_counter()

  def diff(self):
    return round(time.perf_counter() - self.time, 4)

@functools.lru_cache
def fact(n):
  return n * fact(n - 1) if n > 1 else n

def fib(n):
  return fib(n - 1) + fib(n - 2) if n > 1 else n

def main():
  f = Foo(35)

  a = Mark()
  print(f'a: {f.expensive} -> {a.diff()}s')

  b = Mark()
  print(f'b: {f.expensive} -> {b.diff()}s')

if __name__ == '__main__':
  main()

  # a: 9227465 -> 3.0901s
  # b: 9227465 -> 0.0s
