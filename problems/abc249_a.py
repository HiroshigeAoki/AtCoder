A, B, C, D, E, F, X = map(int, input().split())


if X >= A + C:
    t_takahashi = (X // (A + C)) * A
    if X - t_takahashi < A:
        t_takahashi += (X - t_takahashi)
    elif X - t_takahashi >= A:
        t_takahashi += A

elif A < X < A + C:
    t_takahashi = A
else:
    t_takahashi = X

if X >= D + F:
    t_aoki = (X // (D + F)) * D
    if X - t_aoki < D:
        t_aoki += (X - t_aoki)
    elif X - t_aoki >= D:
        t_aoki += D
elif D < X < D + F:
    t_aoki = D
else:
    t_aoki = X

d_takahashi = t_takahashi * B
d_aoki = t_aoki * E

if d_takahashi > d_aoki:
    print('Takahashi')
elif d_aoki > d_takahashi:
    print('Aoki')
elif d_takahashi == d_aoki:
    print('Draw')