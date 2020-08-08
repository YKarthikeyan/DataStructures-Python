import graph
import queue


def bfs(graph):
    q = queue.Queue()
    visited = set()
    for vertex in graph.vertices.values():
        if vertex not in visited:
            q.put(vertex)
            visited.add(vertex)
            while not q.empty():
                v = q.get()
                print(v)
                for adj in v.adjacent_vertices:
                    if adj not in visited:
                        q.put(adj)
                        visited.add(adj)

def dfs(graph):
    visited = set()
    for vertex in graph.vertices.values():
        dfs_util(vertex, visited)

def dfs_util(vertex, visited):
    if vertex in visited:
        return
    visited.add(vertex)
    print(vertex)
    for adj in vertex.adjacent_vertices:
        dfs_util(adj, visited)



if __name__ == "__main__":
    g = graph.Graph(False)
    g.add_edge(1,2,10)
    g.add_edge(2,3,5)
    g.add_edge(1,4,6)

    bfs(g)
    print('\n')
    dfs(g)