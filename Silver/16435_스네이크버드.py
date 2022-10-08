import sys

n, l = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

for i in arr:
    if l == i:
        l += 1
    else:
        print(l)
        break

print(l)