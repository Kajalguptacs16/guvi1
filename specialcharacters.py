n=input()
s=0
for i in n:
    j=ord(i)
    if (48<=j<=57) or (65<=j<=90) or (97<=j<=122):
        continue
    else:
        s+=1
print(s)
