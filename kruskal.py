# 신장 트리(Spanning Tree)는 무방향 연결 그래프가 존재할 때, 그 그래프에서 모든 정점을 포함하도록 간선을 부분적으로 선택하여 만들 수 있는 부분 그래프 입니다.
# 최소 신장 트리는 그 중에서도 가중치가 있는 그래프일 때를 고려합니다.
# 그래프의 간선마다 가중치가 있을 때 간선의 가중치의 합이 최소가 되는 신장 트리를 최소 신장 트리라고 합니다.

def find(node):
    # path compression 기법
    if parent[node] != node:
        parent[node] = find(parent[node])
 
    return parent[node]
 
def union(v, u):
    root1 = find(v)
    root2 = find(u)
 
    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def kruskal(graph):
    global parent, rank
    mst = {}

    # 1. 초기화
    parent = {k:k for k in graph.keys()}
    rank = dict.fromkeys(graph.keys(), 0)

    # 2. 간선 weight 기반 sorting
    edges = []
    for start, l in graph.items():
        for dst, v in l.items():
            edges.append((v, start, dst))
    edges.sort()

    # 3. 간선 연결 (사이클 없는)
    for e in edges:
        w, v, u = e
        if find(v) != find(u):
            union(v, u)
            mst.setdefault(v, {})[u] = w
            mst.setdefault(u, {})[v] = w

    return mst

graph = {
    'A':{'B':7, 'D':5},
    'B':{'A':7, 'C':8, 'D':9, 'E':7},
    'C':{'B':8, 'E':5},
    'D':{'A':5, 'B':9, 'E':7, 'F':6},
    'E':{'B':7, 'C':5, 'D':7, 'F':8, 'G':9},
    'F':{'D':6, 'E':8, 'G':11},
    'G':{'E':9, 'F':11},
}

parent = None
rank = None

print(kruskal(graph))