import sys
n, m = map(int, input().split())

if n > 0:
    arr = list(map(int, sys.stdin.readline().split()))

    cnt = 1
    total = m 

    for i in arr:
        if total < i:
            total = m
            cnt += 1
    
        total -= i
    print(cnt)

else:
    print(0)