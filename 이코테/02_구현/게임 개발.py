N, M = map(int, input().split())
x, y, input_direction = map(int, input().split())

# 북-동-남-서 (direction과 인덱스 맞춰주자)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# map 정보 입력 받기
map_lst = []
for _ in range(N):
  map_lst.append(list(map(int, input().split())))

# 방문한 위치 기억
visited_map_lst = [[0] * M for _ in range(N)]

# 현재 위치
visited_map_lst[x][y] = 1

# 방향처리에 대한 고민 -> 함수로 빼주자 
direction = input_direction
def turn_left():
  global direction
  direction = (direction - 1) % 4

# 시작 위치 포함
# 움직이는 경우의 수 놓고 - 움직이고 - 조건보고 - 결과반영 (or not)
turn_count = 0
while True: 
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 갈 수 있는 경우
  if map_lst[nx][ny] == 0 and visited_map_lst[nx][ny] == 0:
    x = nx
    y = ny
    visited_map_lst[x][y] = 1
    turn_count = 0
    continue
  # 왼쪽 방향이 가본 칸인 경우 
  else:
    turn_count += 1
  
  # 조건 3번
  if turn_count == 4:
    # 현 위치
    nx -= 2 * dx[direction]
    ny -= 2 * dy[direction]

    # 움직인 공간이 바다라면 움직임을 멈춘다
    if map_lst[nx][ny] == 1:
      break
    x = nx
    y = ny
    visited_map_lst[x][y] = 1
    turn_count = 0

result = 0
for row in visited_map_lst:
  for elem in row:
    if elem == 1:
      result += 1

print(result)
