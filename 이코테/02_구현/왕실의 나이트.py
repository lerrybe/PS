location = input()

row = int(location[1])
col = int(ord(location[0]) - ord('a')) + 1
move_lst = [[-1, 2], [1, 2], [-1, -2], [1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

result = 0

for i in range(len(move_lst)):
  curr_row = row + move_lst[i][1]
  curr_col = col + move_lst[i][0]
  
  if curr_row > 8 or curr_row < 1 or curr_col > 8 or curr_col < 1:
    continue
  result += 1 

print(result)
