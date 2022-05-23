n = int(input())
count = 0
new = n

while(new != n or count == 0):
    count += 1
    new = int(str(new%10) + str(((new//10)+(new%10))%10))

print(count)