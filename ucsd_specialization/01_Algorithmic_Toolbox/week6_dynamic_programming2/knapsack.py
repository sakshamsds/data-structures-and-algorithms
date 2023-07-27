from sys import stdin

# dp = optimization problem

def maximum_gold(capacity, weights):
    dp = [[0] * (capacity + 1) for _ in range(len(weights) + 1)]

    for items in range(1, len(weights) + 1):      # iterate items
        for weight in range(1, capacity + 1):        # iterate capacity, weight is the capacity that we are trying to fulfil
            if weight - weights[items - 1] < 0:
                dp[items][weight] = dp[items - 1][weight]
            else:
                dp[items][weight] = max(dp[items - 1][weight], 
                                    dp[items - 1][weight - weights[items - 1]] + weights[items - 1])
                                #   0                           1               knapsack

    # for row in dp:
    #     print(*row, sep='\t')
    return dp[-1][-1]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    # input_capacity = 20
    # input_weights = [4, 5, 5, 6, 6, 10, 9, 8, 8]
    # input_capacity = 10
    # input_weights = [1, 4, 8]
    print(maximum_gold(input_capacity, input_weights))
