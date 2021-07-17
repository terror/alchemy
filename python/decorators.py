def wrap(func):
  print("wow!")
  func()
  print("oo")

def hello():
  print("hello!")

def dec(func):
  def wrap():
    print('Extended behaviour!')
    func()

  return wrap

@dec
def decoratee():
  print('hello!')

if __name__ == '__main__':
  x = wrap
  x(hello)

  decoratee()
