from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    n = len(segments)
    points = []
    # write your code here

    segments.sort(key=lambda x:x.end)
    # print(segments)
    intersection_point = segments[0].end
    points.append(intersection_point)

    for i in range(n):
        if segments[i].start <= intersection_point:
            continue
        else:
            intersection_point = segments[i].end
            points.append(intersection_point)

    return points

if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    # n, *data = 3, 1, 3, 2, 5, 3, 6
    # n, *data = 4, 4, 7, 1, 3, 2, 5, 5, 6
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
