n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)

total = 0 
for i in range(n):
    m = lst[i] - i
    if m > 0 :
        total += m 

print(total)