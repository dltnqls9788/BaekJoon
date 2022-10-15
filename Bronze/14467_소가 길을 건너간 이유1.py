cow_dict = dict()
cnt = 0 

for i in range(int(input())):
    num, point = map(int, input().split())

    if num in cow_dict.keys():
        if point != cow_dict[num]:
            cnt += 1
            cow_dict[num] = point
        else:
            cow_dict[num] = point

print(cnt)