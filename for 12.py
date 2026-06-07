cnt=0

n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        cnt=cnt+1
if cnt == 2:
    print("소수입니다")
else:
    print("소수가 아닙니다")
