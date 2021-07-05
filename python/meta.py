class Meta(type):
  def __new__(cls, what, bases=None, dict=None):
    if 'area' not in dict:
      raise Exception("Area not found!")
    return type.__new__(cls, what, bases, dict)

class Shape(metaclass=Meta):
  def __init__(self, l, w):
    self.l = l
    self.w = w

  def area(self):
    return self.l * self.w

class Square(Shape):
  def __str__(self):
    return f"[Square] Width: {self.w}, Length: {self.l} Area: {self.area()}"

  def area(self):
    return super().area()

class Triangle(Shape):
  def __str__(self):
    return f"[Triangle]: Width: {self.w}, Length: {self.l}, Area: {self.area()}"

  def area(self):
    return (self.l * self.w) // 2

def main():
  print(Square(2, 2))
  print(Triangle(2, 3))

if __name__ == '__main__':
  main()
