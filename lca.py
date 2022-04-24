import collections


def make_tree(N):
    ret = {i: {'parent': [0]*LOG, 'depth': None, 'to': []}
           for i in range(1, N+1)}
    S = tuple(map(int, input().split()))
    for i in range(0, len(S), 2):
        ret[S[i+1]]['parent'][0] = S[i]
        ret[S[i]]['to'].append(S[i+1])
    return ret


def setParent(tr):
    for j in range(1, LOG):
        for i in range(1, V+1):
            tmp = tr[i]['parent'][j-1]
            if tmp:
                tr[i]['parent'][j] = tr[tmp]['parent'][j-1]


def cal_depth(tr):
    dq = collections.deque()
    dq.append(ROOT)
    tr[ROOT]['depth'] = 0
    while dq:
        tmp = dq.popleft()
        for node in tr[tmp]['to']:
            dq.append(node)
            tr[node]['depth'] = tr[tmp]['depth'] + 1


def find_LCA(tr, A, B):
    if tr[A]['depth'] < tr[B]['depth']:
        A, B = B, A

    for i in range(LOG-1, -1, -1):
        if tr[A]['depth'] - tr[B]['depth'] >= (1 << i):
            A = tr[A]['parent'][i]

    if A == B:
        return A

    for i in range(LOG-1, -1, -1):
        if tr[A]['parent'][i] != tr[B]['parent'][i]:
            A = tr[A]['parent'][i]
            B = tr[B]['parent'][i]

    return tr[A]['parent'][0]


def cal_child_cnt(tr, node):
    ret = 0
    dq = collections.deque()
    dq.append(node)
    while dq:
        tmp = dq.popleft()
        ret += 1
        for node in tr[tmp]['to']:
            dq.append(node)
    return ret


LOG = 14
ROOT = 1
V, E, A, B = map(int, input().split())
tr = make_tree(V)
setParent(tr)
cal_depth(tr)
lca = find_LCA(tr, A, B)
print(f'{lca} {cal_child_cnt(tr, lca)}')
