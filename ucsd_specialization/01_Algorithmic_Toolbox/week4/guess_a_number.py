def query(y):
    x = 1618235
    if x == y:
        return 'equal'
    elif x < y:
        return 'smaller'
    else:
        return 'greater'

def guess(lower, upper):
    middle = (lower + upper) // 2
    answer = query(middle)
    print(f'Is x={middle}? It is {answer}.')
    if answer == 'equal':
        return
    elif answer == 'smaller':
        guess(lower, middle - 1)
    else:
        assert answer == 'greater'
        guess(middle + 1, upper)

guess(1, 2097151)

from math import log2

def divide_till_one(n):
    divisions = 0
    while n > 1:
        n = n // 2
        divisions += 1
    return divisions

for d in range(1, 10):
    n = 10 ** d
    print(f'{n} {log2(n)} {divide_till_one(n)}')

    