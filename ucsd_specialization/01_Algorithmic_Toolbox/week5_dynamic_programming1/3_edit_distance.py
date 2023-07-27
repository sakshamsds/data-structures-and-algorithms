def edit_distance(first_string, second_string):

    m = len(first_string)       # first string on column
    n = len(second_string)
    
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
    for i in range(n + 1):
        dp[0][i] = i

    for i in range(m + 1):
        dp[i][0] = i

    # print(dp)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diff = 0 if first_string[i - 1] == second_string[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, 
                           dp[i][j - 1] + 1, 
                           dp[i - 1][j - 1] + diff)


    return dp[-1][-1]


if __name__ == "__main__":
    # print(edit_distance('editing', 'distance'))
    # print(edit_distance('ab', 'ab'))
    # print(edit_distance('horse', 'ros'))
    print(edit_distance(input(), input()))
