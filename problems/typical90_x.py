def main():
    ans = sum([abs(a - b) for a, b in zip(A,B)])
    if ans > K:
        print('No')
    elif (K - ans) % 2 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    main()