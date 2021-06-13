import random

nums = [n for n in range(1, 46)]
*win, bonus = random.sample(nums, 7)
win = set(win)
pick = []
for _ in range(100000):
    pick.append(set(random.sample(nums, 6)))

res = {'1등':0, '2등':0, '3등':0, '4등':0, '5등':0, '꽝':0}
for v in pick:
    hit = len(win.intersection(v))
    if hit == 6:
        res['1등'] += 1
    elif hit == 5 and bonus in v:
        res['2등'] += 1
    elif hit == 5:
        res['3등'] += 1
    elif hit == 4:
        res['4등'] += 1
    elif hit == 3:
        res['5등'] += 1
    else:
        res['꽝'] += 1

print(res)