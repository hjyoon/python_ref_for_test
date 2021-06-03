INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    dist = [[INF]*n for _ in range(n)] # 최단 경로를 담는 배열

    for i in range(n): # 최단 경로를 담는 배열 초기화
        for j in range(n):
            dist[i][j] = graph[i][j]

    for k in range(n): # 거치는 점
        for i in range(n): # 시작 점
            for j in range(n): # 끝 점
                # k를 거쳤을 때의 경로가 더 적은 경로
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

graph = [
        [0, 2, INF, 4],
        [2, 0, INF, 5],
        [3, INF, 0, INF],
        [INF, 2, 1, 0]
    ]

dist = floyd_warshall(graph)
print(*dist, sep='\n')

d = dict()
d['three'] = 3
d['one'] = 1
d['four'] = 4
d['two'] = 2

while d:
    print(d.popitem())

#from heapdict import heapdict