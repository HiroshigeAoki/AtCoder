def main():
    pass

if __name__ == "__main__":
    H, W = map(int, input().split(' '))
    A = [list(map(int, input().split(' '))) for _ in range(H)]

    ANS = [[0 for c in range(W)] for l in range(H)]
    sum_l = [sum(A[l]) for l in range(H)]
    sum_c = [sum([a[c] for a in A]) for c in range(W)]

    for l in range(H):
        for c in range(W):
            ANS[l][c] = str(sum_l[l] + sum_c[c] - A[l][c])
    
    for a in ANS:
        print(' '.join(a))

    main()