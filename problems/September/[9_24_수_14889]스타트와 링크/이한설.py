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


／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／


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
    for arr in permutations(array, 2):
        x, y = arr[0] - 1, arr[1] - 1
        scr += board[x][y]
    return scr

min_value = 100000000

for arr in combinations(nums, N//2):
    res = []
    for idx in range(N):
        if (idx + 1) not in arr:
            res.append(idx+1)
    score_1 = score(list(arr))
    score_2 = score(res)
    min_value = min(min_value, abs(score_1 - score_2))
    if min_value == 0:
        break

print(min_value)


／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
sum_board = [[0] * N for _ in range(N)]

for idx in range(N):
    for jdx in range(N):
        if idx < jdx:
            sum_board[idx][jdx] = board[idx][jdx] + board[jdx][idx]

def score(team):
    scr = 0
    for idx in range(len(team)):
        for jdx in range(idx + 1, len(team)):
            scr += sum_board[team[idx]][team[jdx]]
    return scr

min_value = float("inf")

def backtrack(idx, start, link):
    global min_value

    if idx == N:
        if len(start) == N // 2 and len(link) == N // 2:
            diff = abs(score(start) - score(link))
            min_value = min(min_value, diff)
        return

    if min_value == 0:
        return

    if len(start) < N // 2:
        backtrack(idx + 1, start + [idx], link)

    if len(link) < N // 2:
        backtrack(idx + 1, start, link + [idx])

backtrack(1, [0], [])
print(min_value)


／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／


from itertools import combinations

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
sum_board = [[0] * N for _ in range(N)]

for idx in range(N):
    for jdx in range(N):
        if idx < jdx:
            sum_board[idx][jdx] = board[idx][jdx] + board[jdx][idx]

def score(array):
    scr = 0
    for idx in range(len(array)):
        for jdx in range(idx + 1, len(array)):
            scr += sum_board[array[idx]][array[jdx]]
    return scr

nums = list(range(N))
comb_list = list(combinations(nums, N // 2))
half = len(comb_list)

min_value = float("inf")

for picked in comb_list[:half]:
    start = list(picked)
    link = [x for x in nums if x not in picked]

    score_start = score(start)
    score_link = score(link)

    diff = abs(score_start - score_link)
    
    if diff == 0:  
        min_value = 0
        break

    if diff < min_value:
        min_value = diff

print(min_value)
