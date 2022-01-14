N, K = map(int, input().split())
result = 0

while True:
  # K로 나누어 떨어지는 가장 가까운 수 찾기 (빼는 연산 한 번에 수행)
  target = (N // K) * K
  result += (N - target)
  N = target

  if N < K:
    break

  # 수 찾았으니 K로 나눠주기
  N //= K
  result += 1

# N < K 인 경우 처리
result += N - 1

print(result)
