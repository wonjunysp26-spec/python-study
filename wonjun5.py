x, y = map(int,input().split())
if x == 0 and y == 0:
    print('원점')
elif y == 0:
    print('x축')
elif x == 0:
    print('y축')
else:
    print('축에 있지 않다')
