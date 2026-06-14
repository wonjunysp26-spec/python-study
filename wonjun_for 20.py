a, b= map(int,input().split())
c=0
# a, b 큰 값 보
if a > b:
    c=a
    a=b
    b=c
j=0
jj=0
jjj=0

for i in range(a,b+1):
    if ( i % 7 == 0)and(i % 17 == 0):
        jjj=jjj+1
    elif ( i % 7 ==0):
        j=j+1
    elif ( i % 17 == 0):
        jj=jj+1

print(f'짱수 {j}')
print(f'짱짱수 {jj}')
print(f'짱짱짱수 {jjj}')

