import sys
from unittest import result


data = sys.stdin.readline().rstrip()

cur = 0
stack = []
result = 0

for i in range(len(data)):
    if data[i] == "(":
        stack.append("(")

    else:
        if data[i - 1] == "(":
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1


print(result)
