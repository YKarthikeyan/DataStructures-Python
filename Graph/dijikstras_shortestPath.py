import sys
sys.path.insert(1,'./')
from graph import Graph
from PriorityQueue.priorityQueue import PriorityQueue

def shortest_path(graph, sourceVertex):
    minHeap = PriorityQueue(True)
    distance = {}
    parent = {}

    for vertex in graph.vertices.values():
        minHeap.add_task(sys.maxsize, vertex)

    minHeap.change_task_priority(0, sourceVertex)
    distance[sourceVertex] = 0
    parent[sourceVertex] = None

    while minHeap.is_empty() is False:
        task    = minHeap.peek_task()
        weight  = minHeap.get_task_priority(task)
        current = minHeap.pop_task()
        distance[current] = weight

        for edge in current.edges:
            adjacent = get_other_vertex_for_edge(current, edge)
            if minHeap.contains_task(adjacent) is False:
                continue

            newDistance = distance[current] + edge.weight
            if minHeap.get_task_priority(adjacent) > newDistance:
                minHeap.change_task_priority(newDistance, adjacent)
                parent[adjacent] = current

    return distance


def get_other_vertex_for_edge(vertex, edge):
    if edge.vertex1.id == vertex.id:
        return edge.vertex2
    else:
        return edge.vertex1

if __name__ == '__main__':
    graph = Graph(False)
    graph.add_edge(1,2,5)
    graph.add_edge(2,3,2)
    graph.add_edge(1,4,9)
    graph.add_edge(1,5,3)
    graph.add_edge(5,6,2)
    graph.add_edge(6,4,2)
    graph.add_edge(3,4,3)

    distance = shortest_path(graph, graph.vertices[1])
    print(distance)

