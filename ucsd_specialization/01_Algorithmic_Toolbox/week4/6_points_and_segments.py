from sys import stdin


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


if __name__ == '__main__':
    # data = list(map(int, stdin.read().split()))
    # data = [1, 3, -10, 10, -100, 100, 0]
    data = [3, 2, 0, 5, -3, 2, 7, 10, 1, 6]
    # data = [2, 3, 0, 5, 7, 10, 1, 6, 11]
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    # print(n, m, input_starts, input_ends, input_points)

    output_count = points_cover_naive(input_starts, input_ends, input_points)
    print(*output_count)
