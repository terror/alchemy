from enum import Enum

class OP(Enum):
  ADD = 1
  SUB = 2
  MUL = 3
  DIV = 4
  MOD = 5

d = {
    OP.ADD: lambda x, y: x + y,
    OP.SUB: lambda x, y: x - y,
    OP.MUL: lambda x, y: x * y,
    OP.DIV: lambda x, y: x / y,
    OP.MOD: lambda x, y: x % y
}

if __name__ == '__main__':
  print(d[OP(int(input()))](*map(int, input().split())))
