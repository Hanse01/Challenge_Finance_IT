# 카운팅 정렬!

import sys
input = sys.stdin.readline

N = int(input())
OFFSET = 1000000  # 음수 포함을 위해 offset 사용
SIZE = 2000001    # -1,000,000 ~ 1,000,000 범위

# 카운팅 배열 생성
count = [False] * SIZE

for _ in range(N):
    num = int(input())
    count[num + OFFSET] = True  # 존재 표시

# 출력
for idx in range(SIZE):
    if count[idx]:
        print(idx - OFFSET)
