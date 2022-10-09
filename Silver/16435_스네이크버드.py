import sys

n, l = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

for i in arr:
    if i > l:
        break
    elif i <= l:
        l+=1

print(l)