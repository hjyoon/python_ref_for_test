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
 
parent = {
    'A':'A',
    'B':'B',
    'C':'C',
    'D':'D',
    'E':'E',
    'F':'F',
    'G':'G',
}
rank = dict.fromkeys(parent, 0)

union('B', 'A')
print(parent)

union('D', 'C')
print(parent)

union('D', 'B')
print(parent)