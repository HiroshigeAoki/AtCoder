def main():
    pass

if __name__ == "__main__":
    N = int(input())
    S = set()
    for i in range(N):
        s = input()
        if s in S:
            continue
        else:
            S.add(s)
            print(i + 1)

    main()