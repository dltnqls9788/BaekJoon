n = 4
arr = [2,1,1,0]

# n = int(input())
# arr = list(map(int, input().split()))

ans = [0] * n 

lst = []
list(lst) 

for i in range(1, n+1):
    cnt = arr[i-1] # 2
    r_cnt = 0 

    for j in range(n):
        if cnt == r_cnt and not ans[j]:
            ans[j] = i
            break 
        elif not ans[j]:
            r_cnt += 1 

print(*ans)