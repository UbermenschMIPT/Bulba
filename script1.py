n=int(input())
s=str(input())
for i in range(1,(n+1)//2+1):
    print(i*s)
for i in range(n//2,0,-1):
    print(i*s)

