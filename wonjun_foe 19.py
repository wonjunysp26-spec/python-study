a = int(input("태어난 해를 입력하세요: "))
n = 0

for i in range(a, 2024):
    if (i % 400 == 0) or ( i % 100 != 0 and i % 4 == 0):
        n=n+1
print(n)
        
  
