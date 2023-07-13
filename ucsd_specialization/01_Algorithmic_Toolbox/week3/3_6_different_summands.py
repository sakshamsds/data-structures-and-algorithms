def optimal_summands(n):
    summands = []
    # write your code here

    cur_val = n
    for i in range(1, n+1):
        # print(summands)
        if cur_val - i >= 0:
            summands.append(i)
            cur_val -= i
        else:
            summands.pop()
            summands.append(cur_val + i-1)
            break
    return summands


if __name__ == '__main__':
    n = int(input())
    # n = 6
    # n = 8
    # n = 2
    # n = 10
    # n = 20
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
