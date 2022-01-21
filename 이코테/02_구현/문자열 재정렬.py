string = input()

num_lst = []
alpha_lst = []

for letter in string:
  if letter.isdigit():
    num_lst.append(int(letter))
  else:
    alpha_lst.append(ord(letter))

sum_num = sum(num_lst)
sorted_alpha_lst = sorted(alpha_lst)

result_alpha_lst = []

for letter in sorted_alpha_lst:
  alphabet = chr(letter)
  result_alpha_lst.append(alphabet)

result = ''.join(result_alpha_lst) + str(sum_num)
  
print(result)
