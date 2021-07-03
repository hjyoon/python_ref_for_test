n = 10
sa = [7, 4, 8, 6, 1, 5, 2, 9, 3, 0]
s = [0] * (n+1)

for i in range(n):
    s[sa[i]] = i
s[n] = -1

cnt = 1
for i in range(n-1):
    if s[sa[i]+1] > s[sa[i+1]+1]:
        cnt += 1

print(sa)
print(s)
print(cnt)