import heapq

def prim(start_node, graph):
    mst = {}
    connected_nodes = set(start_node)
    candidate_edge_list = list(map(lambda x:(x[1], start_node, x[0]), graph[start_node].items()))
    heapq.heapify(candidate_edge_list)
    
    while candidate_edge_list:
        weight, n1, n2 = heapq.heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.setdefault(n1, {})[n2] = weight
            mst.setdefault(n2, {})[n1] = weight
            
            for dst, weight in graph[n2].items():
                if dst not in connected_nodes:
                    heapq.heappush(candidate_edge_list, (weight, n2, dst))
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

print(prim('A', graph))

d = {'A': 1, 'B': 2, 'C': 3}

l = list(map(lambda k:(k), d.items()))
print(l)

def computeLPS(pat, lps):
    leng = 0  # length of the previous longest prefix suffix

    # 항상 lps[0]==0이므로 while문은 i==1부터 시작한다.
    i = 1
    while i < len(pat):
        # 이전 인덱스에서 같았다면 다음 인덱스만 비교하면 된다.
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            # 일치하지 않는 경우
            if leng != 0:
                # 이전 인덱스에서는 같았으므로 leng을 줄여서 다시 검사
                leng = lps[leng-1]
                # 다시 검사해야 하므로 i는 증가하지 않음
            else:
                # 이전 인덱스에서도 같지 않았다면 lps[i]는 0 이고 i는 1 증가
                lps[i] = 0
                i += 1

pat = 'ABXABCA'
lps = [0,0,0,0,0,0,0]
computeLPS(pat, lps)
print(lps)