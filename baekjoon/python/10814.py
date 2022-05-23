N = int(input())

result_lst = []
for _ in range(N):
    num_str, name = input().split()
    num = int(num_str)
    result_lst.append([num, name])

result_lst.sort(key = lambda member: [member[0]])

for result in result_lst:
    print(result[0], result[1])
