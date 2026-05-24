height, weight = map(int, input().split())
bim = weight/((height/100)**2)

if bim >= 25:
    category = '비만'
elif bim >= 23:
    category = '과체중'
elif bim >= 18.5:
    category = '정상'
else:
    category = '저체중'

print(f'당신의 bim는 {bim}이며, {category}입니다.')
