N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sorted_a = sorted(A)
sorted_b = sorted(B)

for i in range(N):
  if i + 1 > K:
    break
  if sorted_a[i] >= sorted_b[N - 1 - i]:
    break
  sorted_a[i], sorted_b[N - 1 - i] = sorted_b[N - 1 - i], sorted_a[i]

print(sum(sorted_a))
