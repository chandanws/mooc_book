import sys


class Vertex(object):
    """
    Vertex class: a vertex of a Graph
    """
    def __init__(self):
        self.__color = 'white'
        self.f = 0 # finished order
        self.d = 0 # discovered order
        self.adjacent = []

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        if value == 'grey':
            self.__color = 'grey'
        elif value == 'black':
            self.__color = 'black'
        elif value == 'white':
            self.__color = 'white'
        else:
            raise ValueError("The color of vertex must be white, grey or b")


class Graph(object):
    """
    Graph class: directed
    """

    def __init__(self):
        self.vertexes = {}
        self.visited = {}
        self.finished_nodes = set()
        self.sccs = []

    def add_edge(self, start, end):
        if start in self.vertexes:
            self.vertexes[start].append(end)
        else:
            self.vertexes[start] = [end]

    def __len__(self):
        """
        Return length of Graph
        """
        return len(self.vertexes)

    def transpose(self):
        """
        Compute the transpose of the Graph
        """
        vertexes = self.vertexes
        self.vertexes = {}
        for vertex in vertexes.keys():
            for adjacent in vertexes[vertex]:
                if adjacent in self.vertexes:
                    self.vertexes[adjacent].append(vertex)
                else:
                    self.vertexes[adjacent] = [vertex]

    def dfs(self, order_of_vertex):
        """
        Depth first search for graph
        Input: Class graph
        """
        # initialize
        for vertex in self.vertexes.keys():
            self.visited[vertex] = 0

        for vertex in self.vertexes.keys():
            if self.visited[vertex] == 0:  # unvisted
                print('(', end='')
                stack = [vertex]
                while stack:
                    node = stack.pop()
                    print(')', end='')
                    if self.visited[node] != 0:
                        print('(')
                        self.visited[node] = 1

                        for adjacent in self.vertexes[node]:
                            if self.visited[adjacent] == 0:
                                stack.append(adjacent)
                                print('(', end='')







    def strong_connected_components(self):

        # depth-first-search
        self.dfs(list(self.vertexes.keys()))

        # store finishing order
        finished_order = list(self.finished_nodes)

        # transpose
        #self.transpose()

        # depth-first-search in decreasing finishing order
        #finished_order.reverse()
       # print('again-------------')
        #self.dfs(finished_order)


if __name__ == '__main__':
    # input_file = 'assignment1.txt'
    input_file = 'small_test.txt'
    graph = Graph()
    with open(input_file) as infile:
        for line in infile:
            (start, end) = tuple(int(number) for number in line.split())
            graph.add_edge(start, end)
    graph.strong_connected_components()
    print('the graph is ', graph.vertexes)
    scc_length = []
    for scc in graph.sccs:
        scc_length.append(len(scc))

    scc_length.sort()
    print(graph.sccs)
