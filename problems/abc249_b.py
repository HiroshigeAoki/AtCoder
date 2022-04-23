S = input()

S = [s for s in S]

lower, upper = False, False
for s in S:
    if s.isupper():
        upper = True
        break
for s in S:
    if s.islower():
        lower = True
        break


set_S = set(S)

uniq = True if len(S) == len(set_S) else False

if upper and lower and uniq:
    print('Yes')
else:
    print('No')