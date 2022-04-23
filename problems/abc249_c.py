from collections import Counter
from itertools import combinations

N, K = map(int, input().split())

S = [[s for s in input()] for _ in range(N)]
ANS = 0
for n in range(1, N+1):
    for t in combinations(S, n):
        freq = Counter(list(Counter(sum(t, [])).values()))
        if K in freq:
            m = freq.get(K)
            ANS = m if m > ANS else ANS

print(ANS)
