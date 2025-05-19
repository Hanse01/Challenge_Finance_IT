import sys
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    idx = jdx = 0
    
    # 두 리스트를 병합
    while idx < len(left) and jdx < len(right):
        if left[idx] < right[jdx]:
            result.append(left[idx])
            idx += 1
        else:
            result.append(right[jdx])
            jdx += 1
    
    # 남은 요소들 처리
    result.extend(left[idx:])
    result.extend(right[jdx:])
    
    return result

# 입력 처리
N = int(input())
arr = [int(input()) for _ in range(N)]

# Merge Sort로 정렬
sorted_arr = merge_sort(arr)

# 출력
sys.stdout.write('\n'.join(map(str, sorted_arr)) + '\n')
