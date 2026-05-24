n=int(input())
cut = 0
i = 1
while i <= n:
    if n % i == 0:
        cut=cut + 1

if cut == 2:
    print('소수입니다')
else :
    print('소수가 아닙니다')
