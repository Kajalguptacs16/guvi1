n=5
c=0
for i in range(2,n):
    if(n%i==0):
        c=c+1
if c==0:
    print("yes")
else:
    print("no")
