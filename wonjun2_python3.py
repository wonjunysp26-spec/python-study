c=0

while True:
    n=input()
    if n == '끝':
        break
    elif n[0] == '김':
        c=c+1
print(f'김씨는 {c}명입니다.')
