"""ergonomic exit handlers!

Notes:
    - executed upon normal interpreter termination
    - runs in reverse order in which they were registered
    - will not get called when program is killed by a signal not handled by Python

"""
import atexit
import sys

@atexit.register
def clean():
  print("cleaned!")

def main():
  d = {
    1: 2,
    2: 3,
    3: 4
  }
  c = 0
  for i in range(1, 4):
    c += d[i]
  print("lol!", c)

if __name__ == '__main__':
  main()
  """
  lol! 9
  cleaned!
  """
