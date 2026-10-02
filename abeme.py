mr={"E":"3", "3":"E", "J":"L", "L":"J", "S":"2", "2":"S", "Z":"5", "5":"Z"}
s=str(input())
m=1
p=1
mr1={"A","H","I","M","O","T","U","V","W","X","Y","1","8"}
for i in range (len(s)//2+1):
    if s[i] in mr:
        if s[len(s)-1-i]!=mr[s[i]]:
            m=0
            break
    elif s[i] in mr1:
        if s[i]!=s[len(s)-1-i]:
            m=0
            break
    else:
        m=0
        break
for i in range (len(s)//2+1):
    if s[i]!=s[len(s)-1-i]:
        p=0
        break
if m==1 and p==1:
    print(s+ " is a mirrored palindrome")
elif m==1 and p==0:
    print(s+ " is a mirrored string")
elif m==0 and p==1:
    print(s+ " is a regular palindrome")
else:
    print(s+ " is not a palindrome")
#№2