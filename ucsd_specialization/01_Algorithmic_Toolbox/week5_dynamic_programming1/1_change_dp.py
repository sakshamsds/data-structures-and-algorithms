def change(money):
    # write your code here

    # # recursive solution
    # if money == 1 or money == 3 or money == 4:
    #     return 1
    # if money == 2:
    #     return 2
    
    # return 1 + min(change(money - 1), change(money - 3), change(money - 4))

    coins = [1, 3, 4]
    dp = [0] * (money + 1)
    for m in range(1, money + 1):
        # print(dp)
        dp[m] = float('inf')
        for coin in coins:
            if m >= coin:
                # print(m, coin)
                num_coins = 1 + dp[m - coin]
                dp[m] = min(num_coins, dp[m])

    # print(dp)
    return dp[m]
    

if __name__ == '__main__':
    m = int(input())
    # m = 34
    # m = 10
    print(change(m))
