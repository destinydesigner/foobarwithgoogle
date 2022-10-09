from collections import deque
MAX_CAPACITY = 2000001


def solution(entrances, exits, path):
    vertex_num = len(path)
    total_num = vertex_num + 2

    residual = [[0 for _ in range(total_num)] for _ in range(total_num)]

    for i in range(vertex_num):
        for j in range(vertex_num):
            residual[i+1][j+1] = path[i][j]

    for s in entrances:
        residual[0][s + 1] = MAX_CAPACITY

    for e in exits:
        residual[e + 1][total_num - 1] = MAX_CAPACITY

    def bfs():
        parents = [-1 for _ in range(total_num)]
        queue = deque()
        queue.append(0)
        while queue and parents[-1] == -1:
            u = queue.popleft()
            for v in range(total_num):
                if residual[u][v] > 0 and parents[v] == -1:
                    queue.append(v)
                    parents[v] = u
        path = []
        u = parents[-1]
        while u != 0:
            if u == -1:
                return None
            path.append(u)
            u = parents[u]
        path.reverse()
        return path

    max_flow = 0
    path = bfs()

    while path:
        flow = MAX_CAPACITY
        u = 0
        for v in path:
            flow = min(flow, residual[u][v])
            u = v
        max_flow += flow
        u = 0
        for v in path:
            residual[u][v] -= flow
            residual[v][u] += flow
            u = v
        path = bfs()
    return max_flow
