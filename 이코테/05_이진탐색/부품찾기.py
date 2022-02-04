def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None
  
n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

print(n_list)
for elem in m_list:
  result = binary_search(n_list, elem, 0, n - 1)
  if result == None:
    print('no', end=' ')
  else: 
    print('yes', end=' ')
