def lcs3(first_sequence, second_sequence, third_sequence):
    m = len(first_sequence)        
    n = len(second_sequence)         
    p = len(third_sequence)
    table = [[[0] * (n + 1)  for _ in range(m + 1)] for _ in range(p + 1)]
    # print(table)

    for i in range(1, p + 1):
        for j in range(1, n + 1):
            for k in range(1, m + 1):
                addition = 1 if first_sequence[k - 1] == second_sequence[j - 1] == third_sequence[i - 1] else 0
                table[i][j][j] = max(table[i][j - 1][k],
                                table[i - 1][j][k],
                                table[i][j][k - 1],
                                table[i - 1][j - 1][k - 1] + addition)

    return table[-1][-1][-1]

if __name__ == '__main__':
    # n = int(input())
    # a = list(map(int, input().split()))
    # assert len(a) == n

    # m = int(input())
    # b = list(map(int, input().split()))
    # assert len(b) == m

    # q = int(input())
    # c = list(map(int, input().split()))
    # assert len(c) == q

    a = [8, 3, 2, 1, 7]
    b = [8, 2, 1, 3, 8, 10, 7]
    c = [6, 8, 3, 1, 4, 7]

    print(lcs3(a, b, c))
