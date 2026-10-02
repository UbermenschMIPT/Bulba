def p(n, d=2):
    if n <= 1:
        return []
    if d * d > n:
        return [n]
    if n % d == 0:
        return [d] + p(n // d, d)
    return p(n, d + 1)
n = int(input())
print(p(n))
