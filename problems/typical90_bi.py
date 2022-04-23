from collections import deque

def main():
    pass

if __name__ == "__main__":
    Q = int(input())
    T, X = [], []
    d = deque()
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            d.appendleft(x)
        elif t == 2:
            d.append(x)
        else:
            print(d[x-1])
    main()