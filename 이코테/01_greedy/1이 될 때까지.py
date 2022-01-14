N, K = map(int, input().split())

result = 0

while N >= K:
  while N % K != 0:
    N -= 1
    result += 1
  N //= K
  result += 1

# 1 < N < K 인 경우에 대한 처리
while 1 < N < K:
  N -= 1
  result += 1

# result += N - 1


print(result)
