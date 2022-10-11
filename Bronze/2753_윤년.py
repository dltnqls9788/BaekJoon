# 윤년 - 1 아니면 - 0 
# 윤년 -> 연도가 4의 배수이면서 100의 배수가 아님


n = int(input())

if (n%4==0 and n%100!=0) or n%400==0:
    print(1)
else:
    print(0)