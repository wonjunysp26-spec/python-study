num=int(input())
if num % 7 == 0 and num % 17 == 0:
    print('짱짱짱수')
elif num % 7 == 0:
    print('짱수')
elif num % 17 == 0:
    print('짱짱수')
else:
    print('그냥수')
