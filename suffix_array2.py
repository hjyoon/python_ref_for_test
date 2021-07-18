import sys
input = sys.stdin.readline
s = input().rstrip()
n = len(s)
sa = [0] * n
group = [0] * (n+1)

for i in range(n):
    sa[i] = i

for i in range(n):
    group[i] = s[i]

group[n] = ''

def custom_cmp(x, y, l):
    if group[x] == group[y]:
        return group[min(x+l, n)] < group[min(y+l, n)]
    else:
        return group[x] < group[y]

l = 1
while l//2 < n:
    sa.sort(key=lambda x:(group[x], group[min(x+l, n)]))
    group2 = [0] * (n+1)
    group2[sa[0]] = 0
    group2[n] = -1
    for i in range(1, n):
        if custom_cmp(sa[i-1], sa[i], l):
            group2[sa[i]] = group2[sa[i-1]] + 1
        else:
            group2[sa[i]] = group2[sa[i-1]]
    group = group2
    l *= 2

print(*sa, sep='\n')