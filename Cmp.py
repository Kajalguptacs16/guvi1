li=input().split()
if li[0]==li[1]:
    print(li[0])
else:
    if len(li[0])>len(li[1]):
        print(li[0])
    else:
        print(li[1])
