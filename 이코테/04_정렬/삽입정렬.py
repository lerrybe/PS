array = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

# 선택하는 친구는 인덱스 1부터 시작, 0은 이미 정렬되어 있다고 가정
for i in range(1, len(array)):
  for j in range(i, 0, -1):
    if array[j] < array[j - 1]:
      array[j], array[j - 1] = array[j - 1], array[j]
    else:
      break

print(array)
