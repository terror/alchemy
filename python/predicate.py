def evens(l):
  if not l: return []
  if len(l[0]) % 2 == 0: return [l[0]] + evens(l[1:])
  return evens(l[1:])

def ewords(l):
  if not l: return []
  if 'e' in l[0]: return [l[0]] + evens(l[1:])
  return evens(l[1:])

def pronouns(l):
  if not l: return []
  if l[0] in ["you", "it", "they", "she", "you"]: return [l[0]] + evens(l[1:])
  return evens(l[1:])

def keep(pred, l):
  if not l: return []
  if pred(l[0]): return [l[0]] + keep(pred, l[1:])
  return keep(pred, l[1:])

def main():
  print(keep(lambda x: len(x) % 2 == 0, ["oh", "hi", "the", "awh"]))

if __name__ == '__main__':
  main()
