import time

def filter(func, iterable):
  return [el for el in iterable if func(el)]

def map(func, iterable):
  return [func(x) for x in iterable]

def reduce(func, iterable, init=None):
  it = iter(iterable)
  val = next(it) if init is None else init

  for el in it:
    val = func(val, el)

  return val

def summation(func, N):
  return sum(list(map(func, range(1, N))))

def timer(func):
  def wrap(*args, **kwargs):
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    print(f'Function {func.__name__} executed in {end - start:.4f}s')

  return wrap

@timer
def waste(n):
  for _ in range(n):
    pass
