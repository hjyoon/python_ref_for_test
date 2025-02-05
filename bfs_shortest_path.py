from collections import deque


def bfs_shortest_path(graph, start, end):
    # 방문 여부 및 부모 노드 저장용
    visited = set()
    parent = dict()

    # 시작 정점 초기화
    queue = deque([start])
    visited.add(start)
    parent[start] = None  # 시작 노드는 부모가 없다고 표시

    while queue:
        u = queue.popleft()

        # 목표 정점을 찾으면 즉시 탐색 종료 가능
        if u == end:
            break

        # 인접 정점 순회
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                parent[v] = u
                queue.append(v)

    # 최단 경로 복원
    path = []
    if end in visited:
        # end 노드에서부터 parent를 역추적
        current = end
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()  # 역추적 결과이므로 순서를 뒤집어야 실제 경로가 됨
    else:
        # end 노드에 도달 불가능한 경우
        path = []

    return path


# 사용 예시
graph = {1: [2, 3], 2: [1, 4, 5], 3: [1, 6], 4: [2], 5: [2, 6], 6: [3, 5]}

start_node = 1
end_node = 6

shortest_path = bfs_shortest_path(graph, start_node, end_node)
print("최단 경로:", shortest_path)
