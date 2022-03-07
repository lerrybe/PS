n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))

lost.sort()
reserve.sort()

new_lost = [i for i in lost]
new_reserve = [i for i in reserve]

for student in reserve:
  if student in lost:
    new_lost.remove(student)
    new_reserve.remove(student)

lost_to_reserved = 0

for target in new_lost:
  if (target - 1) in new_reserve:
    new_reserve.remove(target - 1)
    lost_to_reserved += 1
    continue
  if (target + 1) in new_reserve:
    new_reserve.remove(target + 1)
    lost_to_reserved += 1
    continue

answer = n - len(new_lost) + lost_to_reserved

print(answer)
