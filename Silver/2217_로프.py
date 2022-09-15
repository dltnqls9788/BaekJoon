n = int(input())

lope = []
for _ in range(n):
    lope.append(int(input()))

lope.sort()
answer = []
for k in lope:
  answer.append(k*n)
  n -= 1 

print(max(answer))