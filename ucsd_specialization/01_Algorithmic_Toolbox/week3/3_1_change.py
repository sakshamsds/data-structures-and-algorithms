def change(money):
    # write your code here

    # min_coins = money // 10 + (money % 10 // 5) + (money % 10 % 5 // 1)
    min_coins = 0
    denominations = [10, 5, 1]
    idx = 0
    while money>0:
        if money >= denominations[idx]:
            money -= denominations[idx]
            min_coins += 1
        else:
            idx += 1

    return min_coins


if __name__ == '__main__':
    m = int(input())
    # m = 2
    # m = 28
    print(change(m))