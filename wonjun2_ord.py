s=input()
result=''
diff = ord('a') - ord('A')

for c in s:
    if ord(c) >= ord('A') and ord(c) <= ord('Z'):
        result=result+chr(ord(c)+diff)

    else:
        result = result+c

print(result)
