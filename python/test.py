import random

class T:
  store = []

  @staticmethod
  def run():
    status = lambda name, result: f"[{name}] ... {result}"
    for test in T.store:
      try:
        test(); print(status(test.__name__, "PASSED"))
      except: print(status(test.__name__, "FAILED"))

  @staticmethod
  def test(*args, **kwargs):
    def wrap(func):
      T.store.append(func)
    return wrap

  @staticmethod
  def fuzz(fn, n = 10):
    # this just passes in random integers
    def wrap(func):
      for args in [[random.randint(1, 1000000) for i in range(fn.__code__.co_argcount)] for i in range(n)]:
        fn(*args)
      T.store.append(func)
    return wrap

def add(x, y):
  return x + y

def mul(x, y):
  return x * y

def fib(n):
  return fib(n - 1) + fib(n - 2) if n > 1 else n

def main():
  T.run()

@T.test()
def test_add():
  assert add(1, 2) == 3

@T.test()
def test_fib():
  assert fib(0) == 0
  assert fib(1) == 1
  assert fib(14) == 377

@T.test()
def test_mul_a():
  assert mul(0, 1000) == 0

@T.test()
def test_mul_b():
  assert mul(1, 1000) == 0

@T.fuzz(n=10, fn=mul)
def test_mul_c():
  assert mul(1, 1) == 1

if __name__ == '__main__':
  main()
