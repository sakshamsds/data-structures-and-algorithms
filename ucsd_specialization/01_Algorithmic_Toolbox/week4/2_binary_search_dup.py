def binary_search(keys, query):
    # write your code here
    left, right = 0, len(keys) - 1

    while left <= right:
        mid = (left + right) // 2
        if keys[mid] == query and ((mid != 0 and keys[mid - 1] != query) or (mid == 0)):
            return mid
        elif keys[mid] >= query:
            right = mid - 1
        else:
            left = mid + 1

    # while left <= right:
    #     mid = (left + right) // 2
    #     if keys[mid] == query:
    #         break
    #     elif keys[mid] > query:
    #         right = mid - 1
    #     else:
    #         left = mid + 1

    # if keys[mid] == query:
    #     while mid >= 0:
    #         if keys[mid] != query:
    #             return mid + 1
    #         mid -= 1
    #     return 0
    
    return -1


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    
    # input_keys = [2, 4, 4, 4, 7, 7, 9]
    # input_queries = [9, 4, 5, 2]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
