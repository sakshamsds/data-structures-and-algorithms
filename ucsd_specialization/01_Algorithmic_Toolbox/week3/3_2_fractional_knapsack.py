from sys import stdin

def optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    num_items = len(weights)
    value_per_weight = []
    for i in range(num_items):
        value_per_weight.append([i, values[i]/weights[i]])

    # sort
    value_per_weight.sort(key=lambda x : x[1], reverse=True)

    # print(value_per_weight)

    # add
    for i in range(num_items):
        if capacity < 0:
            break
        idx = value_per_weight[i][0]
        min_weight = min(capacity, weights[idx])
        value += min_weight * value_per_weight[i][1]
        capacity -= min_weight

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    # data = [1, 10, 500, 30]
    # data = [3, 50, 60, 20, 100, 50, 120, 30]
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
