n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

total = 0 
for i in range(n):
    if i%3 != 2:
        total += arr[i]

print(total)