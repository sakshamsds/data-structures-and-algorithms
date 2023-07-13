import functools

def largest_number_naive(numbers):
    for i, num in enumerate(numbers):
        numbers[i] = str(num)

    def compare(n1, n2):
        if n1 + n2 > n2 + n1:
            return -1
        return 1

    numbers.sort(key=functools.cmp_to_key(compare))
    return "".join(numbers)


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    # input_numbers = [21, 2]
    # input_numbers = [9, 4, 6, 1, 9]
    # input_numbers = [0, 1]
    print(largest_number_naive(input_numbers))
