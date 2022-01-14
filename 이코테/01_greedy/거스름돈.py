from audioop import reverse
from lib2to3.pgen2.tokenize import untokenize


N = int(input())

remain = N
cnt = 0

unit_lst = [100, 500, 50, 10]
sorted_unit_lst = sorted(unit_lst, reverse=True)

for unit in sorted_unit_lst:
  cnt += remain // unit
  remain = remain % unit

print(cnt)