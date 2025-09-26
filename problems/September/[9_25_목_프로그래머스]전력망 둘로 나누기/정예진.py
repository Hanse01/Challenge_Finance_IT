# 접근 방법
# 1) wires에서 하나씩 간선 제거
# 2) 제거한 간선 기반으로 양방향 트리 그리기 (리스트 활용)
# 3) 제거한 간선과 연결되어 있던 2개 노드 기반으로 트리를 BFS로 순회
# 4) visited 기준으로 각 트리의 노드 개수 파악
# 5) minimum 값 구하기

from collections import deque
def bfs(start, n, ls):
    visited = [0] * (n+1)

    pq = deque()
    visited[start] = 1
    for idx in range(len(ls[start])):
        pq.append((start,ls[start][idx]))

    while pq:
        _, e = pq.popleft()
        if visited[e]:
            continue
        visited[e] = 1
        if not ls[e]:
            continue
        else:
            for i in range(len(ls[e])):
                pq.append((e, ls[e][i]))
    return sum(visited)



def solution(n, wires):
    answer = n
    for idx in range(n-1):
        new_wires = wires[:]
        s = new_wires.pop(idx)
        s1, s2 = s[0], s[1]

        wire_ls = [[] for _ in range(n+1)]

        for s,e in new_wires:
            wire_ls[s].append(e)
            wire_ls[e].append(s)

        tree1 = bfs(s1, n, wire_ls)
        tree2 = bfs(s2, n, wire_ls)
        answer = min(answer, abs(tree1-tree2))

    return answer
