def curry(func):
  def wrap(*args, **kwargs):
    ans = func(*args, **kwargs)

    def r(*args, **kwargs):
      return ans + func(*args, **kwargs)

    return r

  return wrap

@curry
def add(x, y):
  return x + y

if __name__ == '__main__':
  print(add(1, 2)(1, 2)) # 6
