# python 3 only!!!
import collections
import math


class Graph:
    # graph class inspired by https://gist.github.com/econchick/4666413

    def __init__(self):
        self.vertices = set()

        # makes the default value for all vertices an empty list
        self.edges = collections.defaultdict(list)
        self.weights = {}
        self.directions = {}

    def add_vertex(self, value):
        self.vertices.add(value)

    def add_edge(self, from_vertex, to_vertex, distance, direction):
        if from_vertex == to_vertex:
            pass  # no cycles allowed
        self.edges[from_vertex].append(to_vertex)
        self.weights[(from_vertex, to_vertex)] = distance
        self.directions[(from_vertex, to_vertex)] = direction

    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Edges: " + str(self.edges) + "\n"
        string += "Weights: " + str(self.weights)
        return string


def dijkstra(graph, start):
    # initializations
    s = set()
    # delta represents the length shortest distance paths from start -> v, for v in delta.
    # We initialize it so that every vertex has a path of infinity (this line will break if you run python 2)
    delta = dict.fromkeys(list(graph.vertices), math.inf)
    previous = dict.fromkeys(list(graph.vertices), None)

    # then we set the path length of the start vertex to 0
    delta[start] = 0

    # while there exists a vertex v not in S
    while s != graph.vertices:
        # let v be the closest vertex that has not been visited...it will begin at 'start'
        v = min((set(delta.keys()) - s), key=delta.get)

        # for each neighbor of v not in S
        for neighbor in set(graph.edges[v]) - s:
            new_path = delta[v] + graph.weights[v, neighbor]

            # is the new path from neighbor through
            if new_path < delta[neighbor]:
                # since it's optimal, update the shortest path for neighbor
                delta[neighbor] = new_path

                # set the previous vertex of neighbor to v
                previous[neighbor] = v
        s.add(v)

    return delta, previous


def shortest_path(graph, start, end):
    # Uses dijkstra function in order to output the shortest path from start to end

    delta, previous = dijkstra(graph, start)

    path = []
    vertex = end

    while vertex is not None:
        path.append(vertex)
        vertex = previous[vertex]

    path.reverse()
    return path

def robot_commands(g, path):

    if (path[0] == 'n1' or path[0] == 'n19' or path[0] == 'n16'):
        direction = 'North'
    elif (path[0] == 'n3' or path[0] == 'n5'):
        direction = 'West'
    elif (path[0] == 'n6' or path[0] == 'n8' or path[0] == 'n10'):
        direction = 'South'
    elif (path[0] == 'n12' or path[0] == 'n17'):
        direction = 'East'
    else:
        direction = 'North'

    for node in path[:-1]:
        next_node = path[path.index(node) - len(path)+1]
        if direction == "North":
            if g.directions[node, next_node] == "East":
                direction = "East"
                print("Right")
            elif g.directions[node, next_node] == "West":
                direction = "West"
                print("Left")
            elif g.directions[node, next_node] == "South":
                direction = "South"
                print("Turn around")
        elif direction == "South":
            if g.directions[node, next_node] == "East":
                direction = "East"
                print("Left")
            elif g.directions[node, next_node] == "West":
                direction = "West"
                print("Right")
            elif g.directions[node, next_node] == "North":
                direction = "North"
                print("Turn around")
        elif direction == "East":
            if g.directions[node, next_node] == "South":
                direction = "South"
                print("Right")
            elif g.directions[node, next_node] == "North":
                direction = "North"
                print("Left")
            elif g.directions[node, next_node] == "West":
                direction = "West"
                print("Turn around")
        elif direction == "West":
            if g.directions[node, next_node] == "North":
                direction = "North"
                print("Right")
            elif g.directions[node, next_node] == "South":
                direction = "South"
                print("Left")
            elif g.directions[node, next_node] == "East":
                direction = "East"
                print("Turn around")
        print("Forward")


def main():
    g = Graph()
    g.add_vertex('n1')
    g.add_vertex('n2')
    g.add_vertex('n3')
    g.add_vertex('n4')
    g.add_vertex('n5')
    g.add_vertex('n6')
    g.add_vertex('n7')
    g.add_vertex('n8')
    g.add_vertex('n9')
    g.add_vertex('n10')
    g.add_vertex('n11')
    g.add_vertex('n12')
    g.add_vertex('n13')
    g.add_vertex('n14')
    g.add_vertex('n15')
    g.add_vertex('n16')
    g.add_vertex('n17')
    g.add_vertex('n18')
    g.add_vertex('n19')

    g.add_edge('n1', 'n2', 1, "North")
    g.add_edge('n2', 'n1', 1, "South")
    g.add_edge('n2', 'n3', 1, "East")
    g.add_edge('n3', 'n2', 1, "West")
    g.add_edge('n2', 'n4', 1, "North")
    g.add_edge('n4', 'n2', 1, "South")
    g.add_edge('n4', 'n5', 1, "East")
    g.add_edge('n5', 'n4', 1, "West")
    g.add_edge('n4', 'n6', 1, "North")
    g.add_edge('n6', 'n4', 1, "South")
    g.add_edge('n7', 'n4', 1, "East")
    g.add_edge('n4', 'n7', 1, "West")
    g.add_edge('n7', 'n8', 1, "North")
    g.add_edge('n8', 'n7', 1, "South")
    g.add_edge('n7', 'n9', 1, "West")
    g.add_edge('n9', 'n7', 1, "East")
    g.add_edge('n9', 'n10', 1, "East")
    g.add_edge('n10', 'n9', 1, "West")
    g.add_edge('n9', 'n11', 1, "West")
    g.add_edge('n11', 'n9', 1, "East")
    g.add_edge('n11', 'n12', 1, "West")
    g.add_edge('n12', 'n11', 1, "East")
    g.add_edge('n11', 'n13', 1, "South")
    g.add_edge('n13', 'n11', 1, "North")
    g.add_edge('n13', 'n14', 1, "South")
    g.add_edge('n14', 'n13', 1, "North")
    g.add_edge('n14', 'n15', 1, "West")
    g.add_edge('n15', 'n14', 1, "East")
    g.add_edge('n14', 'n16', 1, "South")
    g.add_edge('n16', 'n14', 1, "North")
    g.add_edge('n14', 'n17', 1, "East")
    g.add_edge('n17', 'n14', 1, "West")
    g.add_edge('n17', 'n18', 1, "East")
    g.add_edge('n18', 'n17', 1, "West")
    g.add_edge('n18', 'n19', 1, "South")
    g.add_edge('n19', 'n18', 1, "North")
    g.add_edge('n18', 'n7', 1, "North")
    g.add_edge('n7', 'n18', 1, "South")
    g.add_edge('n13', 'n17', 1, "East")
    g.add_edge('n17', 'n13', 1, "West")

    # print(g)
    # print(g.directions['n2', 'n1'])
    robot_commands(g, shortest_path(g, "n1", "n3"))
    # print(dijkstra(g, 'n1'))
    # print(shortest_path(g, 'n1', 'n7'))


if __name__ == "__main__":
    main()
