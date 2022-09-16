# 최대공약수(Greatest Common Divisor, GCD)
import sys 
import math

for _ in range(int(input())):
    arr = list(map(int, sys.stdin.readline().split()))
    n, nums = arr[0], arr[1:]
    total = 0 

    for i in range(n-1):
        for j in range(i+1, n):
            total += math.gcd(nums[i], nums[j])
    print(total)