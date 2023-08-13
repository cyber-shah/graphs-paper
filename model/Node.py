class NodeRC:

    def __init__(self, name,
                 row=None, column=None, parent=None,
                 g=None, h=None, f=None):
        """
        Constructor for NodeRC. It takes in a name, row, column, g, heuristic, and f.

        :param name: Name of the node
        :param row: Row of the node (int)
        :param column: Column of the node (int)
        :param g: G stands for "cost from the start node to the current node"
        :param h: Heuristic is the estimated cost from the current node to the goal node
        :param f: F is the sum of g and heuristic
        "total estimated cost = g + heuristic"
        """
        self.index = None
        self.name = name
        self.parent = parent
        self.g = g
        self.h = h
        self.f = f
        if row is None or column is None:
            self.row = 0
            self.column = 0
        else:
            self.row = row
            self.column = column

    def get_node(self):
        return self

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def get_neighbors(self, graph):
        # a list of nodes index
        neighbors = []
        for i in range(graph.number_of_nodes):
            if graph.adjacency_matrix[self.index][i] != float('inf') and i != self.index:
                neighbors.append(graph.get_node_via_index(i))
        return neighbors

    def get_index(self):
        return self.index

    def get_name(self):
        return self.name

    def get_g(self):
        return self.g

    def get_h(self):
        return self.h

    def get_f(self):
        return self.f

    def set_row(self, row):
        self.row = row

    def set_column(self, column):
        self.column = column

    def set_index(self, index):
        self.index = index

    def __str__(self):
        return "(" + str(self.row) + ", " + str(self.column) + ")"

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def __gt__(self, other):
        return self.f > other.f

    def __ge__(self, other):
        return self.f >= other.f