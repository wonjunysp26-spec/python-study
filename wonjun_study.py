n=int(input())

seven=n//7

a=0

for i in range(0, seven +1):
    remain = n - 7*i

    if remain % 17 == 0:
        a = 1
if a == 1:
    print('만들 수 있습니다')
else :
    print('만들 수 없다.')
