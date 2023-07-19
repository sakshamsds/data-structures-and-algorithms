def majority_element_naive(elements):
    # for e in elements:
    #     if elements.count(e) > len(elements) / 2:
    #         return 1

    # Boyer - Moore's algorithm
    res, count = 0, 0
    for element in elements:
        if count == 0:
            res = element
        count += (+1 if element == res else -1)

    count = 0
    for element in elements:
        if element == res:
            count += 1

    return int(count > len(elements)//2)


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
    # print(majority_element_naive([2, 3, 9, 2, 2]))
    # print(majority_element_naive([1, 2, 3, 1, 1]))
    # print(majority_element_naive([1, 2, 3, 1]))
    # print(majority_element_naive([1, 2, 3]))
