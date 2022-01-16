str = input()
group_arr = []

for i in range(len(str) - 1):
  if str[i] != str[i + 1]:
    group_arr.append(0)

group_arr.append(0)

result = len(group_arr) // 2

print(result)
