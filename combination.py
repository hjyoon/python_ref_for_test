def nextComb(flag, n, r):
    i = r-1
    while flag[i] >= n-(r-i):
        i -= 1
        if i < 0:
            return False
    
    flag[i] += 1
    while i < r-1:
        flag[i+1] = flag[i] + 1
        i += 1
    return True

l = [0, 0] # 어떤 조합을 선택할지 인덱스가 저장되는 곳
target = ['a', 'b', 'c', 'd']
result = []
while True:
    if not nextComb(l, 4, 2):
        break
    result.append(tuple(map(lambda x:target[x], l)))
print(result)

# 내장 함수 사용
import itertools

print(list(itertools.combinations(target, 2)))