from collections import deque


def differ(x, y):
    total = 0
    for a, b in zip(x, y):
        if a != b:
            total += 1
    if total == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    if target not in words:
        return 0

    visited = set([begin])
    queue = deque([(begin, 0)])  # 현재 단어, 변환 횟수

    while queue:
        cur_word, cnt = queue.popleft()
        if cur_word == target:
            return cnt
        for word in words:
            if word not in visited and differ(cur_word, word):
                visited.add(cur_word)
                queue.append((word, cnt + 1))
    return 0
