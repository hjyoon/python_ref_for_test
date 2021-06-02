
# graph = [
#         [0, 0, 1, 1, 0, 0],
#         [0, 0, 0, 1, 1, 0],
#         [0, 0, 0, 1, 0, 1],
#         [0, 0, 0, 0, 0, 1],
#         [0, 0, 0, 0, 0, 1],
#         [0, 0, 0, 0, 0, 0]
#     ]

graph = {
        0: set([2, 3]),
        1: set([3, 4]),
        2: set([3, 5]),
        3: set([5]),
        4: set([5]),
        5: set()
    }

def topological_sort(graph):
    answer = []
    queue = []
    in_degree = {}

    for k, v in graph.items():
        for w in v:
            in_degree[w] = in_degree.setdefault(w, 0) + 1
        if k not in in_degree:
            in_degree[k] = 0

    for k, v in in_degree.items():
        if v == 0:
            queue.append(k)

    print(queue)

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