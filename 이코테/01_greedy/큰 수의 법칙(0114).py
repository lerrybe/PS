N, M, K = map(int, input().split())
input_lst = list(map(int, input().split()))

sorted_input_lst = sorted(input_lst, reverse=True)
max_num = sorted_input_lst[0]
second_max_num = sorted_input_lst[1]

result = 0
k_count = 0

for _ in range(M):
  if k_count == K:
    result += second_max_num
    k_count = 0
    continue
  result += max_num
  k_count += 1
  
print(result)