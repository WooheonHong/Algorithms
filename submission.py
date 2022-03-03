import sys


def solution_1874():
    n = int(sys.stdin.readline())
    data = [int(sys.stdin.readline()) for _ in range(n)]
    stack = []
    result = ""
    cur = 1
    for i in data:
        while cur <= i:
            stack.append(cur)
            result += "+\n"
            cur += 1

        if stack[-1] != i:
            result = "NO"
            break
        stack.pop()

        result += "-\n"

    print(result)


if __name__ == "__main__":
    solution_1874()
