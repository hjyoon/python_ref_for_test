# 크래머 공식(Cramer’s rule)
# ax + by = c
# dx + ey = f
# 위 연립 1차 방정식에서 a,b,c와 d,e,f가 주어질 때, x,y를 구하는 방법
# 아래는 2x2 연립방정식의 해를 즉시 계산. 단, D != 0 이 아닐 때 유일해 존재.
# D = 0인 경우, 해가 없거나 무수히 많아 공식 적용 불가.

a, b, c = 1, 3, -1
d, e, f = 4, 1, 7
D = a * e - b * d
x = (c * e - b * f) // D
y = (a * f - c * d) // D

print(x, y)
