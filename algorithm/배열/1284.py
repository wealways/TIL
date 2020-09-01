T = int(input())

for tc in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())

    a = P * W
    if W <= R:
        b = Q
    else:
        b = Q + (W - R) * S

    if a >= b:
        result = b
    else:
        result = a
    print('#{} {}'.format(tc, result))