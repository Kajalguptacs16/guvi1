n=int(input())
li=list(map(int,input().split()))
ll=sorted(li)
n1=n//2
if n%2==0:
    print(ll[n1-1],end=" ")
    print(ll[n1])
else:
    print(ll[n1])
