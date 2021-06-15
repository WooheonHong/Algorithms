"""
- collections.defaultdict(ListNode)

존재하지 않는 키를 조회할 경우 자동으로 ListNode의 __init__을 참조하여 생성 
"""

import collections


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size

        if self.table[index].value is None:  # self.table[index] 자체는 존재함
            self.table[index] = ListNode(key, value)
            return

        # solve hash collision by separate chaining
        p = self.table[index]
        while p:
            if p.key == key:  # key가 같은데 value가 다르면 update
                p.value = value
                return
            if p.next is None:  # 없으면 마지막 반복에서 에러
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size

        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번재 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
