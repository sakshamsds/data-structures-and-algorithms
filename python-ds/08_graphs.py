"""
entities - nodes
connections - edges

eg - facebook friends and suggestions - undirected
flight routes - directed graphs

Weighted Graph - edges are weighted
    - flight routes, shortest path = shortest distance

Adjacency Matrix
Adjacency List
"""

# directed graph
class Graph:
    def __init__(self, edges) -> None:
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph dict:", self.graph_dict)


    # find all paths
    def get_paths(self, start, end, path=[]):
        path = path + [start]

        # base case
        if start == end:
            return [path]
        
        # edge case
        if start not in self.graph_dict:
            return []
        
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                paths.append(new_paths[0])
        return paths
    
    
    # find shortest path (min stops)
    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None
        
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path


if __name__ == "__main__":
    
    # use list of tuple
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(edges=routes)
    start = "Mumbai"
    end = "New York"
    print(f"Paths between {start} and {end}: ", route_graph.get_paths(start, end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start, end))
