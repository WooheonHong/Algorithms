import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *


n, k = map(int, sys.stdin.readline().split())  # 여러 숫자
# n, k = 7, 3

arr = list(range(1, n + 1))

results = []
idx = 0
len_arr = n
for i in range(n):
    idx += k - 1
    if idx >= len_arr:
        idx %= len_arr
    # print("len_arr: ", len_arr)
    # print("idx : ", idx)
    # print("results", arr[idx])
    results.append(arr[idx])
    del arr[idx]
    # print("remain arr", arr)
    len_arr -= 1

print(*results)
