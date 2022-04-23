def main():
    if H == 1:
        print(W)
    elif W == 1:
        print(H)
    else:
        print((H - H // 2) * (W - W // 2))

if __name__ == "__main__":
    H, W = map(int, input().split())
    main()