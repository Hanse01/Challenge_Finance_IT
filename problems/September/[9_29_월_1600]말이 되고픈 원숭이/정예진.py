import sys
from collections import deque

K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

delta = [(-1,0),(1,0),(0,-1),(0,1)]
h_delta = [(1,2),(2,1),(-1,2),(2,-1),(1,-2),(-2,1),(-1,-2),(-2,-1)]
visited = [[[0] * (K+1) for _ in range(W)] for _ in range(H)]  # visited 배열 3차원으로 k 몇번 썼는지도 체크

def bfs():
    q = deque([(0, 0, 0, 0)]) # x좌표, y좌표, k횟수, 이동 횟수
    visited[0][0][0] = 1

    while q:
        x, y, k, dist = q.popleft()
        if x == H-1 and y == W-1:
            return dist

        # 원숭이 이동(4방향)
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if 0<=nx<H and 0<=ny<W and not arr[x][y] and not visited[nx][ny][k]:
                visited[nx][ny][k] = 1
                q.append((nx, ny, k, dist+1))

        # 말 이동(8방향) → k < K 일 때만
        if k < K:
            for dx, dy in h_delta:
                nx, ny = x+dx, y+dy
                if 0<=nx<H and 0<=ny<W and not arr[x][y] and not visited[nx][ny][k+1]:
                    visited[nx][ny][k+1] = 1
                    q.append((nx, ny, k+1, dist+1))

    return -1

print(bfs())
