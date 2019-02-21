k=int(input())
f=0
for i in range(2,k):
    if k%i==0:
        f=1
        break
    else:
        continue
if f==0:
    print("yes")
else:
    print("no")
