n,k=input().split()
n=int(n)
k=int(k)
c=0
li=list(map(int,input().split()))
for i in li:
    if i==k:
        c+=1
print(c)
