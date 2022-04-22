def main():
    Sum1, Sum2 = [0 for _ in range(N)], [0 for _ in range(N)]
    for i in range(N):
        if i >= 1:
            Sum1[i] = Sum1[i - 1]
            Sum2[i] = Sum2[i - 1]
        if C[i] == 1:
            Sum1[i] += P[i]
        elif C[i] == 2:
            Sum2[i] += P[i]
    
    for l, r in zip(L, R):
        if l >= 2:
            print(Sum1[r - 1] - Sum1[l - 2], Sum2[r - 1] - Sum2[l - 2])
        elif l < 2:
            print(Sum1[r - 1], Sum2[r - 1])

if __name__ == "__main__":
    N = int(input()) # student num
    C, P = [], [] # C: class, P: score
    for _ in range(N):
        c, p = map(int, input().split())
        C.append(c)
        P.append(p)
    Q = int(input())
    L, R = [], [] # L, R: student id
    for _ in range(Q):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)

    main()