# 최대공약수 구하기 
n, m = map(int, input().split())

def gcd(a, b):
  if a % b == 0:
    return b
  else:
    return gcd(b, a % b)

print(gcd(n, m))
