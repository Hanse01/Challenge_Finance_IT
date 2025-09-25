from collections import defaultdict

def dfs(start, graph, visited, cut):
    stack = [start]
    visited[start] = True
    size = 1
    
    while stack:
        node = stack.pop()
        for nxt in graph[node]:
            if (node, nxt) == cut or (nxt, node) == cut:
                continue
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)
                size += 1
    return size

def solution(n, wires):
    graph = defaultdict(list)
    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)
    
    min_value = n
    for u, v in wires:
        visited = [False] * (n + 1)
        size = dfs(u, graph, visited, (u, v))
        diff = abs(n - 2 * size)
        min_value = min(min_value, diff)
    
    return min_value




from collections import defaultdict, deque

def bfs(n, graph):
    visited = [False] * (n + 1)
    q = deque()
    q.append(1)
    cnt = 0
    while q:
        node = q.popleft()
        for next in graph[node]:
            if not visited[next]:
                cnt += 1
                q.append(next)
                visited[next] = True
    
    return abs(n - 2 * cnt)

def solution(n, wires):
    answer = -1
    min_value = 100000000
    
    for idx in range(len(wires)):
        graph = defaultdict(list)
        for jdx in range(len(wires)):
            if idx == jdx:
                continue
            u, v = wires[jdx]
            graph[u].append(v)
            graph[v].append(u)
        diff = bfs(n, graph)
        if min_value > diff:
            min_value = diff
    
    answer = min_value
    return answer





