n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))

new_lost = sorted([i for i in lost if i not in reserve])
new_reserve = sorted([i for i in reserve if i not in lost])

lost_to_reserved = 0

for target in new_lost:
  if (target - 1) in new_reserve:
    new_reserve.remove(target - 1)
    lost_to_reserved += 1
  elif (target + 1) in new_reserve:
    new_reserve.remove(target + 1)
    lost_to_reserved += 1

answer = n - len(new_lost) + lost_to_reserved

print(answer)
