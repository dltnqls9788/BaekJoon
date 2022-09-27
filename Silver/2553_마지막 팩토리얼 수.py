import math

n = str(math.factorial(int(input())))

for i in range(1, len(n)+1):
    if n[-i] != '0' :
        print(int(n[-i]))
        break