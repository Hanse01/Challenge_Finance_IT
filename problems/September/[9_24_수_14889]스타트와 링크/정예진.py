import sys

N = int(sys.stdin.readline())
skill = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def calculate(li):
    total = 0
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            total += skill[li[i]][li[j]] + skill[li[j]][li[i]]
    return total

def get_synergy():
    A_ls, B_ls = [], []
    for i in range(N):
        if visited[i]:
            A_ls.append(i)
        else:
            B_ls.append(i)

    return calculate(A_ls), calculate(B_ls)

def recur(cnt, prev):
    global min_val
    if cnt == N//2:
        s,l = get_synergy()
        min_val = min(min_val, abs(s-l))
        return

    for member_number in range(prev+1, N):
        if visited[member_number]:
            continue

        visited[member_number] = 1
        recur(cnt+1, member_number)
        visited[member_number] = 0


visited = [0] * N
min_val = 21e8
recur(0,0)
print(min_val)
