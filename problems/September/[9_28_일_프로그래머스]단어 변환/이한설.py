from collections import deque

def different(a, b):
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
        if diff > 1:
            return False
    return diff == 1

def bfs(begin, target, words, visited):
    cnt = 0
    q = deque()
    q.append([begin, 0])
    
    while q:
        now_word, cnt = q.popleft()
        for idx in range(len(words)):
            next_word = words[idx]
            if visited[idx] > cnt + 1 and different(now_word, next_word) == 1:
                visited[idx] = cnt + 1
                q.append([next_word, cnt + 1])
                if next_word == target:
                    return visited[idx]
    return 0

def solution(begin, target, words):
    visited = [100] * len(words)
    words.sort(key = lambda x : len(set(begin) - set(x)))
    if target in words:
        answer = bfs(begin, target, words, visited)
    else:
        answer = 0
    return answer





from collections import defaultdict, deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    L = len(begin)
    pattern_dict = defaultdict(list)
    

    for word in words + [begin]:
        for i in range(L):
            pattern = word[:i] + "*" + word[i+1:]
            pattern_dict[pattern].append(word)
    
    # BFS
    q = deque([(begin, 0)])
    visited = set([begin])
    
    while q:
        word, steps = q.popleft()
        if word == target:
            return steps
        for i in range(L):
            pattern = word[:i] + "*" + word[i+1:]
            for next_word in pattern_dict[pattern]:
                if next_word not in visited:
                    visited.add(next_word)
                    q.append((next_word, steps + 1))
    return 0
