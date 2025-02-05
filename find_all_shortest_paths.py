from collections import deque


def find_all_shortest_paths(graph, start, end):
    # 1. BFS를 이용해 각 노드까지의 최단 거리(dist) 계산
    #    동시에, 해당 노드로 오기 위한 모든 부모(parent)들 저장
    dist = {}
    parents = {}

    # 초기화
    for node in graph:
        dist[node] = float("inf")
        parents[node] = []
    dist[start] = 0

    queue = deque([start])

    while queue:
        current = queue.popleft()

        for nxt in graph[current]:
            # 아직 방문되지 않은 노드인 경우, 최단 거리 갱신 & 부모 등록
            if dist[nxt] == float("inf"):
                dist[nxt] = dist[current] + 1
                parents[nxt].append(current)
                queue.append(nxt)
            # 이미 방문된 노드라도, '동일 최단 거리'로 갈 수 있다면 부모 리스트에 추가
            elif dist[nxt] == dist[current] + 1:
                parents[nxt].append(current)

    # 2. 목표 노드(end)에 도달할 수 없다면 빈 리스트 반환
    if dist[end] == float("inf"):
        return []

    # 3. 목표 노드에서 시작 노드로 '역추적(백트래킹)'하며 모든 경로를 복원
    def backtrack_paths(node):
        # 시작 노드까지 도달한 경우, 경로 리스트 반환
        if node == start:
            return [[start]]

        all_paths = []
        # 해당 노드에 연결된 모든 '부모' 노드들에 대해 경로를 만들어 봄
        for p in parents[node]:
            sub_paths = backtrack_paths(p)  # 부모 노드부터의 경로들
            # 부모 노드 경로 뒤에 현재 노드를 추가
            for sp in sub_paths:
                all_paths.append(sp + [node])
        return all_paths

    # 모든 최단 경로들을 찾아서 반환
    return backtrack_paths(end)


# --------------------------
# 사용 예시
# --------------------------
if __name__ == "__main__":
    # 인접 리스트로 표현된 무가중치 그래프
    graph = {1: [2, 3], 2: [1, 4, 5], 3: [1, 5, 6], 4: [2], 5: [2, 3, 6], 6: [3, 5]}

    start_node = 1
    end_node = 5

    all_shortest_paths = find_all_shortest_paths(graph, start_node, end_node)

    print(f"노드 {start_node}에서 노드 {end_node}까지의 모든 최단 경로:")
    for path in all_shortest_paths:
        print(path)
