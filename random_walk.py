import random

def cal_distance_avg(dst):
    s = 0
    for x, y in dst:
        s += (abs(x) + abs(y))
    s /= len(dst)
    return s

d = [(1,0), (-1,0), (0,1), (0,-1)]
dst = []

for limit in range(10, 2001, 10):
    for _ in range(1000):
        sx, sy = 0, 0
        for _ in range(limit):
            dx, dy = random.choice(d)
            sx += dx
            sy += dy
        dst.append((sx, sy))
    print(f'{limit} : {cal_distance_avg(dst)}')
    dst.clear()