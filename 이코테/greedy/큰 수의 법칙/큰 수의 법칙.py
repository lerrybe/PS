# 반복되는 수열 파악하기, 반복되는 수열의 길이 == K + 1
# M 을 K + 1 로 나눈 몫이 수열이 반복되는 횟수
# 다시 여기에 K를 곱해주면 가장 큰 수가 등장하는 횟수
# 가장 큰 수가 더해지는 횟수 : M / (K + 1) * K + M % (K + 1)

N, M, K = map(int, input().split())
input_list = list(map(int, input().split()))

input_list.sort()
first = input_list[-1]
second = input_list[-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(M / (K + 1) * K)
count += M % (K + 1)

sum = 0
sum += count * first
sum += (M - count) * second 

print(sum)
