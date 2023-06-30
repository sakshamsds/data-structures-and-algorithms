import heapq        # min heap, use negative numbers for max heap

'''
# priority queue 

t1 - 5
t2 - 4
t3 - 7
t4 - 9
t5 - 2
t6 - 6

minheap - child > parent, smallest at the top
maxheap - child < parent, largest at the top
heapify to restructue and fulfil the property again
'''

data = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1]
# data = [-x for x in data]
print(sorted(data))             # O(logN)
# insertion in array takes O(N)
# insertion in heap O(logN)
# deletion in heap O(logN)

heapq.heapify(data)
print(data)

# left child = 2*i + 1
# right child = 2*i + 2
print(type(data))
print(heapq.heappop(data))
print(data)
heapq.heappush(data, 2)
print(data)

heapq._heapify_max(data)
print(data)
