N, M = map(int, input().split())

matrix = []
for _ in range(N):
  input_row = list(map(int, input().split()))
  matrix.append(input_row)

min_lst = []
for row in matrix:
  min_row = min(row)
  min_lst.append(min_row)

result = max(min_lst)

print(result)
