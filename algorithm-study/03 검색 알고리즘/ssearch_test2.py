# seq_search() 함수를 사용하여 특정 인덱스 검색하기

from ssearch_while import seq_search

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

# 여기서는 5.6, "n", "DTS"가 키가 됨.
print(f'{t}에서의 5.6의 인덱스는 {seq_search(t, 5.6)}입니다.')
print(f'{s}에서의 "n"의 인덱스는 {seq_search(s, "n")}입니다.')
print(f'{a}에서의 "DTS"의 인덱스는 {seq_search(a, "DTS")}입니다.')

# 문자열도 시퀀스이기 때문에 괜찮음
