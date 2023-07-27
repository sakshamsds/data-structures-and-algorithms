import math

def compute_operations(n):

    # dp = [math.inf, 0] * (n + 1)
    dp = [[math.inf, 0] for _ in range(n + 2)]
    dp[0][0] = 0

    # operations, +1, *2, *3

    for i in range(1, n + 1):
        count_1 = dp[i - 1][0]   
        if count_1 < dp[i][0]:
            dp[i][0] = count_1 + 1
            dp[i][1] = 1

        if i % 2 == 0:
            count_2 = dp[i//2][0]
            if count_2 < dp[i][0]:
                dp[i][0] = count_2 + 1
                dp[i][1] = 2

        if i % 3 == 0:
            count_3 = dp[i//3][0]
            if count_3 < dp[i][0]:
                dp[i][0] = count_3 + 1
                dp[i][1] = 3

        # dp[i] = min([count_1, count_2, count_3])

    num_ops = dp[n][0]
    # print(dp[n])

    res = []
    pointer = n
    for i in range(num_ops):
        res.append(pointer)
        if dp[pointer][1] == 1:
            pointer -= 1
        else:
            pointer //= dp[pointer][1]

    # print(res[::-1])
    return res[::-1]
    # return []


if __name__ == '__main__':
    # input_n = int(input())
    # input_n = 96234
    input_n = 1
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
