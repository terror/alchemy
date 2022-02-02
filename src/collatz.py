def main():
  mx = j = - 1
  for i in range(1, int(input('N: ')) + 1):
    # start at every number between [1, N]
    steps = 0; curr = i
    while curr != 1:
      if curr & 1:
        curr = (curr * 3) + 1
      else:
        curr //= 2
      steps += 1
    print(f'{i} reached the end in {steps} steps.')
    if steps > mx:
      mx = steps; j = i
  print(f'Max steps: {mx}, for number {j}.')

if __name__ == '__main__':
  main()
