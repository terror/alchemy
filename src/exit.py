# Ergonomic exit handlers!
#
# Notes:
#   - executed upon normal interpreter termination
#   - runs in reverse order in which they were registered
#   - will not get called when program is killed by a signal not handled by Python

import atexit
import sys

@atexit.register
def clean():
  print("cleaned")

def main(L):
  print(sum(L))

if __name__ == '__main__':
  main([1, 2, 3])
