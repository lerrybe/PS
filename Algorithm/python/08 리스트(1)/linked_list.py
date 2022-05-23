# 포인터로 연결 리스트 구현하기

from __future__ import annotations 
from typing import Any, Type

class Node:
    """연결 리스트용 노드 클래스"""

    # 1. 클래스의 생성자에 (1) data를 인자로 받아서 self.data에 저장 / (2) 뒤쪽 노드를 참조하는 값인 next를 인자로 받아서 self.next에 저장 
    
    # data는 Any형인데 디폴트는 없고, next는 우리가 만들어 준 Node형인데 일단은 뒤쪽 노드가 없으므로 None으로 지정 
    def __init__(self, data: Any = None, next: Node = None): 
        """초기화"""
        self.data = data  # 데이터
        self.next = next  # 뒤쪽 포인터 


class LinkedList:
    """연결 리스트 클래스"""
    def __init__(self) -> None:
        """초기화"""
        # 변수 선언하듯
        self.no = 0  # 노드의 개수
        self.head = None  # 머리 노드
        self.current = None  # 주목 노드 

    def __len__(self) -> int:
        """연결 리스트의 노드 개수를 반환"""
        return self.no

    def search(self, data:Any) -> int:
        """data와 값이 같은 노드를 검색"""
        cnt = 0  # 몇 번째 노드인지 
        ptr = self.head  # 스캔 중인 노드 변수, 정확히는 스캔 중인 노드를 참조하기 위한 변수 
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr 
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool:
        """연결 리스트에 data가 포함되어 있는지 확인"""
        return self.search(data) >= 0

    def add_first(self, data: Any) -> None:
        """맨 앞에 노드를 삽입"""
        ptr = self.head  # 삽입하기 전의 머리노드
        self.head = self.current = Node(data, ptr)
        self.no += 1

    def add_last(self, data: Any):
        """맨 끝에 노드를 삽입"""
        if self.head is None:
            self.add_first(data)
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data, None)
            self.no += 1 

    def remove_first(self) -> None:
        """머리 노드를 삭제"""
        if self.head is not None:
            self.head = self.current = self.head.next
        self.no -= 1

    def remove_last(self):
        """꼬리 노드를 삭제"""
        if self.head is not None:  # 머리 노드는 있는데 
            if self.head.next is None:  # 그 다음 노드가 없음 == 노드가 1개 
                self.remove_first()
            else: 
                ptr = self.head  # 스캔 중인 노드
                pre = self.head  # 스캔 중인 노드의 앞쪽 노드 , 일단 둘 다 head로 초기화

                while ptr.next is not None:  # 꼬리 노드가 아니라면 
                    pre = ptr
                    ptr = ptr.next  # 스캔 하나씩 밀기
                
                pre.next = None 
                self.current = pre
                self.no -= 1

    def remove(self, p: Node) -> None:
        """노드 p를 삭제"""
        if self.head is not None:  # 리스트가 비어있지 않음
            if p is self.head:  # 노드 P가 존재하는데 그게 머리노드일 때 
                self.remove_first()
            else:  # 노드 p가 존재하는데 그게 머리노드가 아닐 때 
                ptr = self.head

                while ptr.next is not p:  # ptr.next가 p와 같아지만 while문 종료, ptr.next = p.next로
                    ptr = ptr.next  # 탐색 과정
                    if ptr is None:  # 끝까지 다 봤으면 
                        return   # 종료 
                    
                ptr.next = p.next  # 찾았다!  
                self.current = ptr  # 주목 노드를 현재 보는 포인터로 바꿔주고 
                self.no -= 1
    
    def remove_current_node(self) -> None:
        """주목 노드를 삭제"""
        self.remove(self.current)

    def clear(self) -> None:
        """전체 노드를 삭제"""
        while self.head is not None:  # 전체가 비어있을 때까지 
            self.remove_first()  # 머리 노드를 삭제해 감
        self.current = None
        self.no = 0

    def next(self) -> bool:
        """주목 노드를 한 칸 뒤로 이동"""
        if self.current is None or self.current.next is None:
            return False  # 이동 불가
        self.current = self.current.next
        return True

    def print_current_node(self) -> None:
        """주목 노드를출력"""
        if self.current is None:
            print("주목 노드가 존재하지 않습니다.")
        else:
            print(self.current.data)

    def print(self) -> None:
        """모든 노드를 출력"""
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next


    # 이터레이터의 구현
    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
