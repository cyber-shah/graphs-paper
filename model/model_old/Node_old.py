class Node:

    def __init__(self, name, x=None, y=None):
        self.index = None
        self.name = name
        if x is None or y is None:
            self.x = 0
            self.y = 0
        else:
            self.x = x
            self.y = y

    def get_node(self):
        return self

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_neighbors(self, graph):
        # a list of nodes
        neighbors = []
        for i in range(graph.number_of_nodes):
            if graph.adjacency_matrix[self.index][i] != float('inf') and i != self.index:
                neighbors.append(graph.get_node_via_index(i))
        return neighbors

    def get_index(self):
        return self.index

    def get_name(self):
        return self.name

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_index(self, index):
        self.index = index

    def __str__(self):
        return str(self.x) + " " + str(self.y)
