
graph = {
        0: {2, 3},
        1: {3, 4},
        2: {3, 5},
        3: {5},
        4: {5},
        5: {}
    }

def topological_sort(graph:dict):
    answer = []
    queue = []
    in_degree = {}

    for k, v in graph.items():
        in_degree.setdefault(k, 0)
        for w in v:
            in_degree[w] = in_degree.setdefault(w, 0) + 1

    for k, v in in_degree.items():
        if v == 0:
            queue.append(k)

    while queue:
        answer.append(queue)
        new_arr = []
        for i in queue:
            for idx in graph[i]:
                in_degree[idx] -= 1
                if in_degree[idx] == 0:
                    new_arr.append(idx)
        queue = new_arr

    return answer


print(topological_sort(graph))