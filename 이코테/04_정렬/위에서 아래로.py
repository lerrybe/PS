n = int(input())

array = []
for _ in range(n):
  array.append(int(input()))

result = sorted(array)

for num in result[::-1]:
  print(num, end=' ')
