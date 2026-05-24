n=int(input())
clap=0
while n > 0:
    if n%10==3 or n%10==6 or n%10==9:
        clap=clap+1
    n=n//10
print(clap)
