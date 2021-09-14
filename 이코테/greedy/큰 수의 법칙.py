# k <= M
N, M, K = map(int, input().split())
input_list = list(map(int, input().split()))

input_list.sort()
first = input_list[-1]
second = input_list[-2]

count = 0
sum = 0

while True:
    for i in range(K):
        if count == M:
            break
        sum += first
        count += 1
    
    if count == M:
        break
    sum += second
    count += 1

print(sum)
