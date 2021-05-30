"""
리스트 수 : k
리스트 원소 수 : n 
힙에 원소를 힙에 넣었다 뺀다 : 2logn 
--> O(2knlogkn)
"""

import collections
import heapq
from typing import List


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return self.val


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    for i, ls in enumerate(lists):
        for j in range(len(ls) - 1):
            lists[i] = ListNode(ls[j], ListNode(ls[j + 1]))

    s = Solution()
    s.mergeKLists(lists)
