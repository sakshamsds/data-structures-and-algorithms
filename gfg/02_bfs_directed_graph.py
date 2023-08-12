#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        visited, res = set(), [0]
        visited.add(0)
        q = Queue()
        q.put(0)
        
        while not q.empty():
            # print(list(q.queue))
            node = q.get()

            for neighbor in adj[node]:
                if neighbor not in visited:
                    q.put(neighbor)
                    visited.add(neighbor)
                    res.append(neighbor)
                    
        return res

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		# print()
        

# } Driver Code Ends