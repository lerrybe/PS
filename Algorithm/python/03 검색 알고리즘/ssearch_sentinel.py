# 선형 검색은 반복할 때마다 두 가지 종료 조건 체크 
# 종료 조건을 검사하는 비용을 무시할 수 없음
# 이 비용 반으로 줄이기 위해 '보초법!'⭕️ sentinel method 

# 검색할 값과 같은 원소(보초)를 발견했습니다! 
"""
검색할 값을 배열의 맨 끝에 추가 
저장하는 값을 보초라고 부름.
보초는 검색하는 키와 같은 값으로 추가 

그림 b처럼 찾는 값이 우너래 데이터에 존재하지 않아도 a[7]의 보초까지 스캔하는 단계에서 선형 검색의 종료 조건 2(검색할 값과 같은 원소 찾음?)이 성립함.
따라서 선형 검색의 종료조건 1은 판단할 필요가 없음! 
이처럼 보초는 반복을 종료하는 판단 횟수를 줄이는 역할을 함.

실습 3-3은 실습 3-1에 보초법을 반영하여 수정한 프로그램! 
"""

from typing import Any, Sequence
import copy 

def seq_search(seq: Sequence, key: Any) -> int:
    """시퀀스 seq에서 key와 일치하는 원소를 선형 검색(보초법)"""
    """
    깊은 복사는 내부에 객체들까지 모두 새롭게 copy 되는 것
    copy.deepcopy메소드가 해결해주고, a를 변경해도 b가 변경되지 않음 
    """
    a = copy.deepcopy(seq)  # seq를 깊은복사한 후, 
    a.append(key)  # 보초 key를 추가 

    i = 0
    while True: 
        if a[i] == key:
            break
        i += 1 
    return -1 if i == len(seq) else i  # 개수 즉 인덱스 +1 이랑 같으면 -1 출력, 그렇지 않으면 해당 인덱스 출력 

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값을 입력하세요.: '))
    idx = seq_search(x, ky)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else: 
        print(f'검색값은 x[{idx}]에 있습니다.') 

"""
큰 플로우:
1) 배열 개수만큼 만들기
2) 반복문 돌면서 배열 개수만큼 input 받기 
3) 검색할 값 입력 받기
4) 정의한 함수 이용해 검색값 찾기 
"""




