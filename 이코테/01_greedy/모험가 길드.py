N = int(input())
fear_lst = list(map(int, input().split()))
sorted_fear_lst = sorted(fear_lst)

group_cnt = 0
member_cnt = 0

for i in range(len(sorted_fear_lst)):
  x = sorted_fear_lst[i]
  member_cnt += 1
  if member_cnt == x:
    member_cnt = 0
    group_cnt += 1

print(group_cnt)
