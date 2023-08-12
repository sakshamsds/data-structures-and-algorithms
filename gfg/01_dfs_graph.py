#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        visited = [False] * V
        # visited = set()
        res = []
        self.dfs(0, adj, visited, res)
        return res
    
    def dfs(self, node, adj, visited, res):
        res.append(node)
        visited[node] = True
        # visited.add(node)
        for neighbor in adj[node]:      # traverse all neighbors
            if not visited[neighbor]:
            # if neighbor not in visited:
                self.dfs(neighbor, adj, visited, res)


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends