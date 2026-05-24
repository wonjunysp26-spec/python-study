n=int(input())
sum=0
i=0
while  n != -1:
    i=i+1
    if i%2 == 1:
        sum +=n
    n = int(input())
print(sum)
