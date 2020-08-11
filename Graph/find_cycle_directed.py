from graph import Graph

def has_cycle(graph):
    white = set()
    grey = set()
    black = set()

    for vertex in graph.vertices.values():
        white.add(vertex)

    while len(white) > 0:
        current = next(iter(white))
        if dfs(current, white, grey, black) == True:
            return True

    return False

def dfs(vertex, white, grey, black):
    move_vertex(vertex, white, grey)
    for adjacent in vertex.adjacent_vertices:
        if adjacent in black:
            continue
        if adjacent in grey:
            return True
        if dfs(adjacent, white, grey, black) == True:
            return True

    move_vertex(vertex, grey, black)
    return False

def move_vertex(vertex, sourceSet, destinationSet):
    sourceSet.remove(vertex)
    destinationSet.add(vertex)

if __name__ == '__main__':
    graph = Graph(True)
    graph.add_edge(1,2)
    graph.add_edge(1,3)
    graph.add_edge(2,3)
    graph.add_edge(4,1)
    graph.add_edge(4,5)
    graph.add_edge(5,6)
    graph.add_edge(6,4)

    print(has_cycle(graph))