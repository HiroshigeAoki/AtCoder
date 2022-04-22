import math

def main():
    gcd = math.gcd(math.gcd(A, B), C)
    print((A // gcd - 1) + (B // gcd - 1) + (C // gcd - 1))
    

if __name__ == "__main__":
    A, B, C = map(int, input().split())
    main()