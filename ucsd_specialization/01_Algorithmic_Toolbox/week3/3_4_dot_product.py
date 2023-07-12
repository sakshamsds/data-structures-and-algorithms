from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    # max_product = 0
    # for permutation in permutations(second_sequence):
    #     print(permutation)
    #     dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
    #     max_product = max(max_product, dot_product)
    # O(n!)

    pdt = 0
    first_sequence.sort()
    second_sequence.sort()

    for i, j in zip(first_sequence, second_sequence):
        pdt += i * j

    return pdt


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    # print(max_dot_product([2, 3, 9], [7, 4, 2]))
    # print(max_dot_product([23], [39]))
    
