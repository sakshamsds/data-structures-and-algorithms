from sys import stdin


def min_refills(distance, tank, stops):
    # write your code here
    refills = 0
    total_tank = tank
    stops.append(distance)
    num_stops = len(stops)

    for i in range(num_stops - 1):
        # print(total_tank)
        if total_tank < stops[i] or total_tank + tank < stops[i+1]:
            return -1
        
        # check if it need refueling at the current stop
        if total_tank < stops[i+1]:
            total_tank += tank - (total_tank - stops[i])
            refills += 1

    return refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
    # print(min_refills(950, 400, [200, 375, 550, 750]))
    # print(min_refills(200, 250, [100, 150]))
    # print(min_refills(10, 3, [1, 2, 5, 9]))
