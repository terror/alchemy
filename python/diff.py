def diff_a(a, b):
  return list(set(a) - set(b)) + list(set(b) - set(a))

def diff_b(lists):
  x = [list(set(i) - set(j)) for i in lists for j in lists]
  return list(set([item for sublist in x for item in sublist]))

def main():
  a = [1, 2, 3]
  b = [1, 2, 5, 4]
  c = [1, 3, 5, 6]
  print(diff_a(a, b)) # [3, 5, 4]
  print(diff_b([a, b, c])) # [2, 3, 4, 5, 6]

if __name__ == '__main__':
  main()
