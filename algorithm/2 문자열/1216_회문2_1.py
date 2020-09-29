import sys
sys.stdin = open('1216.txt', 'r')

T = 10

def palindrome(matrix, N):
    for M in range(N, 0, -1):
        for i in range(N):
            for j in range(0, N - M +1):
                lst = matrix[i][j:j+M]
                if lst == lst[::-1]:
                    return M

for tc in range(1, T+1):
    t = input()
    N = 100
    matrix = [list(input()) for _ in range(N)]
    answer1 = palindrome(matrix, N)

    for i in range(N):
        for j in range(N):
            if i > j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    answer2 = palindrome(matrix, N)

    if answer1 > answer2:
        answer = answer1
    else:
        answer = answer2



    print('#{} {}'.format(tc, answer))