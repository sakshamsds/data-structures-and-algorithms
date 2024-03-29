# from itertools import combinations

# def inversions_naive(a):
#     number_of_inversions = 0
#     for i, j in combinations(range(len(a)), 2):
#         if a[i] > a[j]:
#             number_of_inversions += 1
#     return number_of_inversions


def merge_sort(elements):
    if len(elements) == 1:
        return elements, 0
    mid = len(elements) // 2
    left, left_count = merge_sort(elements[:mid])
    right, right_count = merge_sort(elements[mid:])
    elements_sorted, merge_count = merge(left, right)
    return elements_sorted, left_count + right_count + merge_count
    

def merge(left, right):
    res = []
    count, i, j = 0, 0, 0
    n, m = len(left), len(right)

    while i < n and j < m:
        if left[i] > right[j]:
            res.append(right[j])
            j += 1
            count += len(left[i:])
        else:
            res.append(left[i])
            i += 1

    res.extend(left[i:])
    res.extend(right[j:])
    return res, count


if __name__ == '__main__':
    # input_n = int(input())
    # elements = list(map(int, input().split()))
    # assert len(elements) == input_n
    # elements = [2, 3, 9, 2, 9]
    # elements = [3, 2, 1]
    # elements = [5, 4, 3, 2, 1] 
    # elements = [2]
    # elements = [9, 8, 7, 3, 2, 1]
    # elements = [3, 3, 18, 2, 5]
    # elements = [1, 1, 1, 1]
    # elements = [1, 0, 2]
    # elements = [1, 2, 0]
    elements = [0, 1, 3, 2]
    print(merge_sort(elements)[1])
    # print(inversions_naive(elements))
