import graph

def topological_sort(graph):
    stack = []
    visited = set()
    for vertex in graph.vertices.values():
        if vertex in visited:
            continue
        topological_sort_util(vertex, stack, visited)
    return stack

def topological_sort_util(vertex, stack, visited):
    visited.add(vertex)
    for adj in vertex.adjacent_vertices:
        if adj in visited:
            continue
        topological_sort_util(adj, stack, visited)
    stack.append(vertex)



if __name__ == '__main__':
    graph = graph.Graph(True)
    graph.add_edge(1,3)
    graph.add_edge(1,2)
    graph.add_edge(3,4)
    graph.add_edge(5,6)
    graph.add_edge(6,3)
    graph.add_edge(3,8)
    graph.add_edge(8,11)

    stack = topological_sort(graph)

    print(stack) #bottom-to-top
    print(stack[::-1]) #top-to-bottom