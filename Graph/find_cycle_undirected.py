import sys
sys.path.insert(1, './')
from graph import Graph
from DisjointSet.disjointSet import DisjointSet

def has_cycle_using_disjoint_set(graph):
    ds = DisjointSet()

    for vertex in graph.vertices.values():
        ds.make_set(vertex.id)

    for edge in graph.edges:
        parent1 = ds.find_set(edge.vertex1.id)
        parent2 = ds.find_set(edge.vertex2.id)

        if parent1 == parent2:
            return True
        else:
            ds.union(edge.vertex1.id, edge.vertex2.id)

    return False

def has_cycle_dfs(graph):
    visited = set()
    for vertex in graph.vertices.values():
        if vertex in visited:
            continue
        flag = has_cycle_dfs_util(vertex, visited, None)
        if flag:
            return True
    return False

def has_cycle_dfs_util(vertex, visited, parent):
    visited.add(vertex)
    for adjacent in vertex.adjacent_vertices:
        if parent is not None and adjacent == parent: #parent is already explored
            continue
        if adjacent in visited:
            return True
        has_cycle = has_cycle_dfs_util(adjacent, visited, vertex)
        if has_cycle:
            return True
    return False

if __name__ == '__main__':
    graph = Graph(False)
    graph.add_edge(0,1)
    graph.add_edge(1,2)
    graph.add_edge(0,3)
    graph.add_edge(3,4)
    graph.add_edge(4,5)
    graph.add_edge(5,1)

    has_cycle1 = has_cycle_dfs(graph)
    has_cycle2 = has_cycle_using_disjoint_set(graph)
    print(str(has_cycle1) + " " + str(has_cycle2))