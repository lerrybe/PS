N = input()

num_list = []
for num in N:
    num_list.append(int(num))

num_list.sort(reverse=True)

print("".join(map(str, num_list)))