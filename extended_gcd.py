# 확장 유클리드 알고리즘
# ax + by = gcd(a,b) 일 때, x, y, gcd(a, b)를 동시에 구하기
def extended_gcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

print(extended_gcd(3, 11))