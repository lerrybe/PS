int_lst = list(map(int, input()))
result_lst = []

for i in range(len(int_lst)):
  result_lst.append(f'{int_lst[i]}')
  if i == len(int_lst) - 1:
    break
  if int_lst[i] <= 1 or int_lst[i + 1] <= 1:
    result_lst.append('+')
  else:
    result_lst.append('*')

# 배열 문자열로 합치기 
result_str = ''.join(result_lst)

# 문자열 그대로 계산하기 (eval)
print(eval(result_str))
