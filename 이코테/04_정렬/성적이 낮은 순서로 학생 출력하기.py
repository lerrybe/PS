n = int(input())

array = []
for _ in range(n):
  name, age_str = input().split()
  age = int(age_str)
  array.append((name, age))

result = sorted(array, key=lambda x : x[1])

for student in result:
  print(student[0], end=' ')
