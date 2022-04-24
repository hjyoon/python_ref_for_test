# 사전순에서의 다음 순열
import itertools


def nextPerm(s):
    i = len(s)-2
    j = 0
    while i >= 0 and s[i] >= s[i+1]:
        i -= 1

    if i == -1:
        return None
    else:
        j = i+1
        while j < len(s) and s[j] > s[i]:
            j += 1
        s[i], s[j-1] = s[j-1], s[i]
        return s[:i+1] + s[:i:-1]


#print(nextPerm(['a', 'b', 'c']))

# 내장 함수 사용

#print(list(itertools.permutations(['a', 'b', 'c'])))

# dfs로 구현
def perm(visit, pos, ac):
    visit[pos] = 1
    ac.append(pos)

    if len(ac) == len(visit):
        print(*ac)
    else:
        for i in range(len(visit)):
            if visit[i] == 0:
                perm(visit, i, ac)

    ac.pop()
    visit[pos] = 0


N = 3
for i in range(N):
    visit = [0] * N
    perm(visit, i, [])
