n, k = map(int, input().split())

lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)

cnt = 0
for i in lst:
    if i <= k:
        cnt += k // i
        k = k % i 
    
    if k == 0:
        break

print(cnt)