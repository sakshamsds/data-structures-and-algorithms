def lcs2(first_sequence, second_sequence):
    n = len(first_sequence)         # num_cols
    m = len(second_sequence)        # num_rows
    table = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): table[i][0] = 0
    for i in range(n + 1): table[0][i] = 0
    # print(table)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            addition = 1 if first_sequence[j - 1] == second_sequence[i - 1] else 0
            table[i][j] = max(table[i][j - 1],
                              table[i - 1][j],
                              table[i - 1][j - 1] + addition)

    return table[-1][-1]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    # a = [2, 7, 5]
    # b = [2, 5]
    # a = [7]
    # b = [1, 2, 3, 4]
    # a = [2, 7, 8, 3]
    # b = [5, 2, 8, 7]

    print(lcs2(a, b))
