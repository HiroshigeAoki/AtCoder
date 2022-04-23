import math
import re

N, K = input().split()
K = int(K)
def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)

for _ in range(K):
    ten = str(int(str(N), 8))
    N = base10int(int(ten), 9)
    N = N.replace('8', '5')

ten = int(N, 8)
print(re.sub(r'^0o', '', oct(ten)))