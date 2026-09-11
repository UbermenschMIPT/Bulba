a=int(input())
b=str(input())
c=""
for i in range(0,len(b),3):
    c+=b[i:i+a+1:-1]
print(c)