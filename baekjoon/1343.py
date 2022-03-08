input_board = input()

# 입력 -> 'XX.XX'
# 출력 -> ['XX', '.', 'XX'] 
def divide_board(board):
    point = 0
    count = 1
    answer_lst = []
    
    if len(board) == 1:
        return [board]

    for i in range(len(board) - 1):
        if board[i] == board[i + 1]:
            count += 1
        elif board[i] != board[i + 1]:
            answer_lst.append(board[point:i + 1])
            point = i + 1
            count = 1

    answer_lst.append(board[point:i + 2])
    return answer_lst


def solution(board):
    result_lst = []

    for target in divide_board(board):
        if target[0] == '.':
            result_lst.append(target)
        else:
            num = len(target)
            if num % 2 == 1:
                return -1
            else:
                result_lst.append('A' * (num // 4) * 4 + 'B' * (num % 4))

    return ''.join(result_lst)

print(solution(input_board))
