graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3},
}

def bellman_ford(graph, start):
    distance, predecessor = dict(), dict()
    for node in graph:
        distance[node] = float('inf')
        predecessor[node] = None
    distance[start] = 0

    # 정점 개수 (V-1) 만큼 반복
    for _ in range(len(graph)-1):
        for node in graph:
            for neighbor in graph[node]:
                # 현재 정점을 거쳐 가는 거리가 더 작을 경우
                if distance[neighbor] > distance[node] + graph[node][neighbor]:
                    distance[neighbor] = distance[node] + graph[node][neighbor]
                    # 거쳐온 바로 이전 노드 저장
                    predecessor[neighbor] = node

    # 음수 사이클 판별
    for node in graph:
        for neighbor in graph[node]:
            if distance[neighbor] > distance[node] + graph[node][neighbor]:
                return -1
    
    #return distance, predecessor
    return distance

print(bellman_ford(graph, 'A'))