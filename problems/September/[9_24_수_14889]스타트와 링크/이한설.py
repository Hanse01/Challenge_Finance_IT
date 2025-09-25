from itertools import combinations, permutations

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

nums = []
for idx in range(N):
    nums.append(idx + 1)

start = 0
link = 0

def score(array):
    scr = 0
    for idx in range(len(array)):
        for jdx in range(idx + 1, len(array)):
            x, y = array[idx] - 1, array[jdx] - 1
            scr += board[x][y] + board[y][x]
    return scr

min_value = 100000000

for arr in combinations(nums, N//2):
    res = []
    for idx in range(N):
        if (idx + 1) not in arr:
            res.append(idx+1)
    score_1 = score(list(arr))
    score_2 = score(res)
    if min_value > abs(score_1 - score_2):
        min_value = abs(score_1 - score_2)
    if min_value == 0:
        break

print(min_value)
