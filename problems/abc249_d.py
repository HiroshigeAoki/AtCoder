from itertools import permutations

N = int(input())

A = list(map(int, input().split()))

ANS = 0
for i, j, k in permutations(A, 3):
    ANS += 1 if int(i/j) == k else 0
print(ANS)
