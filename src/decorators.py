def A(func):
  print("wow!")
  func()
  print("oo")

def B():
  print("hello!")

def C(func):
  def wrap():
    print('Extended behaviour!')
    func()
  return wrap

@C
def D():
  print('hello!')

if __name__ == '__main__':
  A(B)
  D()
