import sys
import re
import collections
import itertools
import math
DEBUG = 0

TC = [
    {'data': [1, [[5, [4, 1, 5, 2, 3], 5, [1, 3, 7, 9, 5]]]], 'AC': '1\n1\n0\n0\n1'},
]
'''
1
5
4 1 5 2 3
5
1 3 7 9 5
'''

def read_data(l, in_f, out_f=None):
    input = in_f.readline
    #N, S = map(lambda x:x.rstrip(), in_f)
    T = int(input().rstrip())
    C = []
    for _ in range(T):
        N = int(input().rstrip())
        S = map(int, input().rstrip().split())
        M = int(input().rstrip())
        S2 = map(int, input().rstrip().split())
        C.append([N, S, M, S2])

    data = [T, C]
    if DEBUG:
        #ac = out_f.readline().rstrip()
        ac = '\n'.join(map(lambda x:x.rstrip(), out_f))
        l.append({'data':data, 'AC':ac})
    else:
        l.append({'data':data})
    

def solution(T, C):
    ans = []
    for i in range(T):
        N, S, M, S2 = C[i]
        S = {k : True for k in S}
        for v in S2:
            if v in S:
                ans.append(1)
            else:
                ans.append(0)
    return ans_to_str(ans)

def ans_to_str(ans):
    if type(ans) == list:
        return '\n'.join(map(str, ans))
    elif type(ans) != str:
        return str(ans)
    else:
        return ans

def main():
    if DEBUG:
        #print_data()
        #print(TC)
        pass
    else:
        TC.clear()
        read_data(TC, sys.stdin)
        #read_data(TC, open('input.txt', 'r'))

    for i, v in enumerate(TC, 1):
        res = solution(*v['data'])
        if DEBUG:
            if res == v['AC']:
                print(f'case #{i}: OK')
            else:
                print(f'case #{i}: ERR')
                print('accepted:')
                print(v['AC'])
                print('wrong answer:')
                print(res)
        else:
            print(res)

def print_data():
    with open("input.txt", 'r') as in_f, open("output.txt", 'r') as out_f:
        tmp = []
        read_data(tmp, in_f, out_f)
        print(tmp)

if __name__ == "__main__":
    main()