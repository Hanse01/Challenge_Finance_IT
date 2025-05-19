N = int(input())
people = list(map(int, input().split()))
people.sort()
    
score = 0

for idx in range(1, N + 1):
    score += people[idx - 1] * (N + 1 - idx)
    
print(score)
