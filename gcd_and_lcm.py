# 유클리드 호제법
def gcd(x, y):
   while y:
       x, y = y, x % y
   return x

def lcm(x, y):
   return x * y // gcd(x,y)

print(gcd(1071, 1029))
print(lcm(1071, 1029))

# 내장함수 사용
import math

print(math.gcd(1071, 1029))
print(math.lcm(1071, 1029))

# 리스트 내의 여러 원소들에 대한 결과도 구할 수 있음.
print(math.gcd(*[2, 6, 8, 14]))
print(math.lcm(*[2, 6, 8, 14]))