#https://logicalbear.net/%E3%80%90%E7%AB%B6%E3%83%97%E3%83%AD%E5%85%B8%E5%9E%8B90%E5%95%8F%E3%80%91%E3%80%8C055-select-5%EF%BC%88%E2%98%852%EF%BC%89-%E3%80%8D%E8%A7%A3%E6%B3%95/
from itertools import combinations
import sys
input = sys.stdin.readline

def main():
    comb = combinations(A, 5)
    cnt = 0
    for c in comb:
        if c[0]%P*c[1]%P*c[2]%P*c[3]%P*c[4]%P == Q:
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    N, P, Q = map(int, input().split())
    A = list(map(int, input().split()))
    main()