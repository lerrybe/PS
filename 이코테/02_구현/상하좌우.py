N = int(input())
move_lst = list(input().split())

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
direction = ['L', 'R', 'U', 'D']

for move in move_lst:
  for i in range(4):
    if move == direction[i]:
      nx = x + dx[i]
      ny = y + dy[i]

  if nx < 1 or nx > N or ny < 1 or ny > N:
    continue
  x, y = nx, ny

print(x, y)
