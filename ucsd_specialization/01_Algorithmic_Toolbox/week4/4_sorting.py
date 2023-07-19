from random import randint

'''
RandomizedQuickSort(c):
if c consists of a single element:
return c
randomly select an element m from c
determine the set of elements csmall smaller than m
determine the set of elements clarge larger than m
RandomizedQuickSort(csmall)
RandomizedQuickSort(clarge)
combine csmall, m, and clarge into a sorted array csorted
return csorted

'''

# https://walkccc.me/CLRS/Chap07/Problems/7-2/

def partition3(array, left, right):
    # write your code here
    # partition index is the first one
    pivot = array[left]
    low = left
    high = left
    # print(array[left:right+1], low, high, 0, pivot)

    for j in range(left + 1, right + 1):
        if array[j] < pivot:
            array[j], array[high + 1] = array[high + 1], array[j]
            array[high + 1], array[low] = array[low], array[high + 1]
            # temp = array[j]
            # array[j] = array[high + 1]
            # array[high + 1] = array[low]
            # array[low] = temp
            low += 1
            high += 1
        elif array[j] == pivot:
            array[high + 1], array[j] = array[j], array[high + 1]
            high += 1
        # print(array[left:right+1], low, high, j)
    return low, high


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    # elements = [2, 3, 9, 2, 9]
    # input_n = len(elements)
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
