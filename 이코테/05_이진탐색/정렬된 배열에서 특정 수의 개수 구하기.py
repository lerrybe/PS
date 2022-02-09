from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
lst = list(map(int, input().split()))

def count_num(list, target):
  left = bisect_left(list, target)
  right = bisect_right(list, target)
  if left == right:
    return -1
  return right - left

print(count_num(lst, x))