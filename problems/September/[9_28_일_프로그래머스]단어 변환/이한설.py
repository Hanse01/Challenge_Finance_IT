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


//////////////////////////////////////////////////////////////////////
# 딕셔너리 활용 패턴 딕셔너리 


from collections import defaultdict, deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    Length = len(begin)
    pattern_dict = defaultdict(list)
    

    for word in words + [begin]:
        for i in range(Length):
            pattern = word[:i] + "*" + word[i+1:]
            pattern_dict[pattern].append(word)
    
    # BFS
    q = deque([(begin, 0)])
    visited = set([begin])
    
    while q:
        word, steps = q.popleft()
        if word == target:
            return steps
        for i in range(Length):
            pattern = word[:i] + "*" + word[i+1:]
            for next_word in pattern_dict[pattern]:
                if next_word not in visited:
                    visited.add(next_word)
                    q.append((next_word, steps + 1))
    return 0


/////////////////////////////////////////////////////////////////////
# 트라이 자료구조 활용


from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # 단어 끝이면 저장

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word

    # word와 한 글자만 다른 모든 단어 찾기
    def search_one_diff(self, word):
        results = []

        def dfs(node, i, diff):
            # diff > 1이면 중단
            if diff > 1:
                return
            # 끝까지 왔을 때
            if i == len(word):
                if node.word and diff == 1:
                    results.append(node.word)
                return
            
            for ch, child in node.children.items():
                if ch == word[i]:
                    dfs(child, i + 1, diff)
                else:
                    dfs(child, i + 1, diff + 1)

        dfs(self.root, 0, 0)
        return results
    
def print_trie(node, indent="", last=True):
    """트라이 구조를 트리 모양으로 예쁘게 출력"""
    # 단어 끝에 도달했으면 표시
    if node.word:
        print(indent + ("└── " if last else "├── ") + f"[{node.word}]")
    # 자식 출력
    children = list(node.children.items())
    for i, (ch, child) in enumerate(children):
        is_last = (i == len(children) - 1)
        print(indent + ("└── " if last else "├── ") + ch)
        new_indent = indent + ("    " if last else "│   ")
        print_trie(child, new_indent, is_last)

def solution(begin, target, words):
    if target not in words:
        return 0

    trie = Trie()
    for w in words:
        trie.insert(w)
    
    print_trie(trie.root)
    q = deque([(begin, 0)])
    visited = set([begin])

    while q:
        word, steps = q.popleft()
        if word == target:
            return steps
        for nxt in trie.search_one_diff(word):
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, steps + 1))

    return 0
