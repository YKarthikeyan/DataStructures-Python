class Vertex(object):
    def __init__(self, id):
        self.id = id
        self.edges = []
        self.adjacent_vertices  = []

    def add_adjacent_vertex(self, vertex, edge):
        self.edges.append(edge)
        self.adjacent_vertices.append(vertex)

    def get_degree(self):
        return len(self.edges)

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return str("Vertex-" + str(self.id))

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

class Edge(object):
    def __init__(self, vertex1, vertex2, isDirected, weight):
        self.vertex1    = vertex1
        self.vertex2    = vertex2
        self.isDirected = isDirected
        self.weight     = weight

    def __eq__(self, other):
        return self.vertex1.id == other.vertex1.id and self.vertex2.id == other.vertex2.id

    def __hash(self):
        return hash(self.vertex1) + hash(self.vertex2)

    def __str__(self):
        return "Edge " + str(self.vertex1) + " " + str(self.vertex2) + " Weight-" + str(self.weight)

    def __repr__(self):
        return self.__str__()

class Graph(object):
    def __init__(self, isDirected):
        self.vertices   = {}
        self.edges      = []
        self.isDirected = isDirected

    def add_edge(self, id1, id2, weight=0):
        if id1 in self.vertices:
            vertex1 = self.vertices[id1]
        else:
            vertex1 = Vertex(id1)
            self.vertices[id1] = vertex1

        if id2 in self.vertices:
            vertex2 = self.vertices[id2]
        else:
            vertex2 = Vertex(id2)
            self.vertices[id2] = vertex2

        edge = Edge(vertex1, vertex2, self.isDirected, weight)
        self.edges.append(edge)

        vertex1.add_adjacent_vertex(vertex2, edge)
        if not self.isDirected:
            vertex2.add_adjacent_vertex(vertex1, edge)

if __name__ == '__main__':
    g = Graph(False)
    g.add_edge(1,2,10)
    g.add_edge(2,3,5)
    g.add_edge(1,4,6)

    for edge in g.edges:
        print(edge)

    for vertex in g.vertices:
        print("Vertex " + str(g.vertices[vertex]))
        for edge in g.vertices[vertex].edges:
            print("Edge " + str(edge))
