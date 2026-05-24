temp = 20
while temp < 100:
    print(f'물은 현재 {temp}도 입니다.')
    heat = int(input('몇 도 올릴까요: '))
    temp += heat
print("물이 끓습니다.")
