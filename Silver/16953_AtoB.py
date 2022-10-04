a, b = map(int, input().split())
r = 1 

while(b!=a):
    r+=1
    test = b
    if b%10 == 1:
        b//=10
    elif b%2 == 0:
        b//=2
    
    if test == b: # 위의 조건에 아무것도 해당하지 못하고 그대로 내려올 경우
        print(-1)
        break 
else:
    print(r)