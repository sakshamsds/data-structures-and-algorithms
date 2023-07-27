def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def min_max(i, j, m, M, ops):
    min_val = float('inf')
    max_val = float('-inf')
    for k in range(i, j):
        a = evaluate(M[i][k], M[k + 1][j], ops[k])
        b = evaluate(m[i][k], M[k + 1][j], ops[k])
        c = evaluate(M[i][k], m[k + 1][j], ops[k])
        d = evaluate(m[i][k], m[k + 1][j], ops[k])
        min_val = min(min_val, a, b, c, d)  
        max_val = max(max_val, a, b, c, d)
    return min_val, max_val


def maximum_value(dataset):
    # write your code here
    ops = dataset[1::2]
    digits = [int(x) for x in dataset[0::2]]
    n = len(digits)
    # print(ops)
    # print(digits)
    m = [[0] * n for _ in range(n)]
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        m[i][i] = digits[i]
        M[i][i] = digits[i]

    for s in range(1, n):
        # print()
        for i in range(n - s):
            j = i + s
            # print(i, j)
            m[i][j], M[i][j] = min_max(i, j, m, M, ops)

    # for row in m:
    #     print(*row, sep='\t')
    # print()
    # for row in M:
    #     print(*row, sep='\t')

    return M[0][n - 1]


if __name__ == "__main__":
    # print(maximum_value("5-8+7*4-8+9"))
    print(maximum_value(input()))
