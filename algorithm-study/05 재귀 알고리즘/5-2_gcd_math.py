import math

print('두 정숫값의 최대 공약수를 구합니다.')
x = int(input('첫 번째 정숫값을 입력하세요.: '))
y = int(input('두 번째 정숫값을 입력하세요.: '))

# 최대 공약수를 구하는 gcd() 함수를 제공
print(math.gcd(x, y))
