import sys
from collections import defaultdict
import bisect

input = sys.stdin.read

def preprocess(heights, n):
    position_map = defaultdict(list)
    for i in range(n):
        position_map[heights[i]].append(i + 1)
    return position_map

def count_in_range(position_list, l, r):
    return bisect.bisect_right(position_list, r) - bisect.bisect_left(position_list, l)

def find_majority_height(n, m, heights, queries):
    position_map = preprocess(heights, n)
    results = []

    for l, r in queries:
        majority = (r - l + 1) // 2
        found = 0
        for key in set(heights[l-1:r]):
            count = count_in_range(position_map[key], l, r)
            if count > majority:
                found = key
                break
        results.append(found)

    return results

# Input parsing
data = input().split()
n, m = int(data[0]), int(data[1])
heights = list(map(int, data[2:n+2]))
queries = [tuple(map(int, data[n+2+i*2:n+4+i*2])) for i in range(m)]

# Solve
results = find_majority_height(n, m, heights, queries)

# Output results
sys.stdout.write("\n".join(map(str, results)) + "\n")