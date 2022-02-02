from typing import List

R, C = 3, 3

def construct(board: List[List[int]]) -> str:
  ret = ""
  for i in range(R):
    for j in range(C):
      if board[i][j] == 2:
        ret += "| X |"
      elif board[i][j] == 1:
        ret += "| O |"
      else:
        ret += "|   |"
    ret += "\n"
  return ret

def won(board: List[List[int]]) -> bool:
  for i in range(R):
    if len(set(board[i])) == 1 and 0 not in board[i]:
      return True

  columns = list(zip(*board))
  for i in range(C):
    if len(set(columns[i])) == 1 and 0 not in columns[i]:
      return True

  diag1, diag2 = [r[i] for i, r in enumerate(board)], [r[-i - 1] for i, r in enumerate(board)]
  if (len(set(diag1)) == 1 and 0 not in diag1
      or (len(set(diag2)) == 1 and 0 not in diag2)):
    return True

  return False

def valid(r: int, c: int, board: List[List[int]]) -> bool:
  return not (r >= R or r < 0 or c >= C or c < 0 or board[r][c])

def full(board: List[List[int]]) -> bool:
  for i in range(len(board)):
    for j in range(len(board)):
      if board[i][j] == 0:
        return False
  return True

def main() -> None:
  board = [[0, 0, 0] for i in range(R)]
  print("Player 1: 'O'\nPlayer 2: 'X'\n")

  p = 1
  while not won(board):
    if full(board):
      print("Tie!")
      exit()

    r, c = map(int, input("Player {} move: ".format(1 if p else 2)).split())

    if not valid(r, c, board):
      print("Invalid move.\n")
      continue

    board[r][c] = 1 if p else 2
    print("Board:\n{}\n".format(construct(board)))

    p ^= 1

  print("Player {} Wins!".format(1 if p ^ 1 else 2))

if __name__ == "__main__":
  main()
