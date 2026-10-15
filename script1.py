n, w = map(int, input().split())
m = list(map(int, input().split()))
c = list(map(int, input().split()))
d = []
r = [[0 for _ in range(n+1)] for _ in range(w+1)]
for i in range(1,n+1):
    for j in range(1,w+1):
        if m[i-1] <= j:
            a = d[i-1][j]
            b = d[i-1][j-m[i-1]] + c[i-1]
            if a > b:
                d[i][j] = a
            else:
                d[i][j] = b
        else:
            d[i][j] = d[i-1][j]
print(d[n][w])
p = []
k = w
for i in range(n, 0, -1):
    if d[i][k] != d[i-1][k]:
        p.append(i)
        k = k - m[i-1]
p.reverse()
print(*p)
