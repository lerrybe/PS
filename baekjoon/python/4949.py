s = input()
s_lst = list(s)
store = []
result = True

# s_lst 탐색하는 과정에서 pop이나 지워주기 
# 스택으로 따로 빼주기
for i in range(len(s_lst)):
    if i == 0 and (s_lst[i] == ')' or s_lst[i] == '}' or s_lst[i] == ']'):
        result = False
        break
    if s_lst[i] == '(':
        store.append(s_lst[i])
    elif s_lst[i] == '[':
        store.append(s_lst[i])
    elif s_lst[i] == ')':
        if store[-1] == '(':
            store.pop()
        else: 
            result = False
            break
    elif s_lst[i] == ']':
        if store[-1] == '[':
            store.pop()
        else: 
            result = False
            break

print(result)

