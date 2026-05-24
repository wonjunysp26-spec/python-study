n = int(input())
i=2
while n != 1:
    if n % i != 0:
        i=i+1
    else:
        print(i)
        n=n//i
        i=2
