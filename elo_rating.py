import math
import collections
import itertools
import random
import copy

DEFAULT_ELO = 1000
K = 30

class Unit:
    def __init__(self, name, hp, atk, atk_times, avd):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.atk_times = atk_times
        self.avd = avd
        self.elo = DEFAULT_ELO
        self.cal_ability_idx()

    def cal_ability_idx(self):
        self.ability_idx = pow(10, (self.elo - DEFAULT_ELO) / 400)

    def update_elo_rating(self, variance):
        self.elo += variance
        self.cal_ability_idx()

def cal_diff_two_ability_idx(winner:Unit, loser:Unit):
        tmp = winner.ability_idx / loser.ability_idx
        return tmp / (tmp+1)

def cal_elo_from_battle_result(winner:Unit, loser:Unit):
    expected_win_rate = cal_diff_two_ability_idx(winner=winner, loser=loser)
    point_value = round(K * (1 - expected_win_rate))
    winner.update_elo_rating(point_value)
    loser.update_elo_rating(-point_value)

def battle(first:Unit, second:Unit):
    a = copy.deepcopy(first)
    b = copy.deepcopy(second)
    while True:
        if a.hp <= 0:
            cal_elo_from_battle_result(winner=second, loser=first)
            return
        elif b.hp <= 0:
            cal_elo_from_battle_result(winner=first, loser=second)
            return
        else:
            while a.atk_times != 0 and b.atk_times != 0:
                if a.atk_times > 0:
                    if random.random() < (1 - b.avd):
                        b.hp -= a.atk
                        a.atk_times -= 1
                    else:
                        a.atk_times -= 1
                else:
                    pass

                if b.atk_times > 0:
                    if random.random() < (1 - a.avd):
                        a.hp -= b.atk
                        b.atk_times -= 1
                    else:
                        b.atk_times -= 1
                else:
                    pass
            a.atk_times = first.atk_times
            b.atk_times = second.atk_times

l = [
    Unit(name='A1', hp=30, atk=6, atk_times=4, avd=0.6),
    Unit(name='B1', hp=40, atk=5, atk_times=4, avd=0.4),
    Unit(name='C1', hp=50, atk=12, atk_times=2, avd=0.2),
    Unit(name='D1', hp=22, atk=5, atk_times=5, avd=0.7),
    Unit(name='E1', hp=35, atk=8, atk_times=3, avd=0.5),
    Unit(name='F1', hp=28, atk=28, atk_times=1, avd=0.5),
    Unit(name='G1', hp=18, atk=3, atk_times=7, avd=0.97)
]

for _ in range(100):
    for a, b in itertools.combinations(l, 2):
        battle(first=a, second=b)
        battle(first=b, second=a)

for u in l:
    print(u.name, u.elo)