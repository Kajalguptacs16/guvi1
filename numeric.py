n=input()
s=0
for i in n:
    j=ord(i)
    if 48<=j<=57:
        s+=1
    else:
        continue
print(s)
