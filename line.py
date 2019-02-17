n=input()
s=0
for i in n:
    if i==".":
        s+=1
    else:
        continue
if n[-1]==".":
    print(s)
else:
    print(s+1)
