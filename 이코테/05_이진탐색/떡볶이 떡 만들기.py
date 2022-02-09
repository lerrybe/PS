n, m = map(int, input().split())
input_lst = list(map(int, input().split()))
start = 0
end = max(input_lst)
target = 0

def cut_and_sum(lst, height):
  sum_num = 0
  for x in lst:
    if x > height:
      sum_num += x - height
  return sum_num

while start <= end:
  all_length = 0
  mid = (start + end) // 2
  all_length = cut_and_sum(input_lst, mid)

  if all_length < m:
    end = mid - 1
  else:
    target = mid
    start = mid + 1

print(target)
