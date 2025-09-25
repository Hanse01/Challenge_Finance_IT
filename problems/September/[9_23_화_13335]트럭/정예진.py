import sys
from collections import deque
# N : 트럭의 수
# W : 다리 길이
# L : 다리 최대 하중
# truck : 트럭들의 무게
# 다리 위에는 w대의 트럭이 동시에 올라갈 수 있으며, 각 트럭은 단위시간에 단위길이만큼 이동
# 동시에 다리 위에 올라가 있는 트럭들의 무게의 합은 다리의 최대 하중인 L보다 작아야 한다

N, W, L = map(int, sys.stdin.readline().split())
truck = list(map(int, sys.stdin.readline().split()))
bridge = deque(0 for _ in range(W))
bridge_weight = 0
time = 0
i = 0

while bridge_weight or i < N:
    left = bridge.popleft()
    bridge_weight -= left
    if i == N:
        bridge.append(0)
    else:
        if bridge_weight + truck[i] <= L:
            bridge_weight += truck[i]
            bridge.append(truck[i])
            i += 1
        else:
            bridge.append(0)
    time += 1

print(time)
