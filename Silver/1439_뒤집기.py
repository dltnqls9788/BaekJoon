import sys

s = str(sys.stdin.readline())
one, zero = 0, 0 

if s[0] == '0':
    zero += 1 
else:
    one += 1

for i in range(1,len(s)):
    if s[i] == '0' and s[i]!=s[i-1]:  
        zero += 1
    elif s[i] == '1' and s[i]!=s[i-1]:
        one += 1

if zero >= one:
    print(one)
else:
    print(zero)