n=int(input())
n1=n
res=0
while(n1!=0):
    rem=n1%10
    res=res+rem*rem*rem
    n1=n1//10
if n==res:
    print("yes")
else:
    print("no")
    
