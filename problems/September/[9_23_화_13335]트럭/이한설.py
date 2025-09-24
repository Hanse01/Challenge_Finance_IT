from collections import deque

N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = deque([0] * W)
time = 0
weight_on_bridge = 0

for truck in trucks:
    while True:
        time += 1
        out = bridge.popleft()
        weight_on_bridge -= out

        if weight_on_bridge + truck <= L:
            bridge.append(truck)
            weight_on_bridge += truck
            break
        else:
            bridge.append(0) 

time += W
print(time)






from collections import deque

N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))

time = 0
on_bridge = deque()  # (무게, 내리는 시각)
weight = 0

for t in trucks:
    while True:
        time += 1

        # 다리에서 내릴 트럭
        if on_bridge and on_bridge[0][1] == time:
            w, _ = on_bridge.popleft()
            weight -= w

        # 새로운 트럭 확인
        if weight + t <= L and len(on_bridge) < W:
            on_bridge.append((t, time + W))  # W 초 뒤 내려감
            weight += t
            break

time = on_bridge[-1][1]
print(time)

