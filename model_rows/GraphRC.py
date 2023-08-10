class GraphRC:
    def __init__(self):
        self.number_of_nodes = 0
        self.number_of_edges = 0
        # Use a list of lists for the adjacency matrix
        self.adjacency_matrix = []
        # Use a dictionary key, value = (x pos, y pos), node
        self.nodesDictionary = {}
        # Use a dictionary key, value = index, node
        self.nodeIndices = {}
        # Use a dictionary key, value = name, node
        self.nodeNames = {}

    def add_node(self, node):
        # 1. Update the node's index
        node.set_index(self.number_of_nodes)
        # 2. Update the graph's dictionary of nodes, adding the new node
        self.nodesDictionary[(node.row, node.column)] = node
        self.nodeIndices[node.get_index()] = node
        self.nodeNames[node.get_name()] = node
        # 3. Update the graph's adjacency matrix
        self.number_of_nodes += 1

        # Update the adjacency matrix with a new row and column for the new node
        new_row = [float('inf')] * self.number_of_nodes
        for row in self.adjacency_matrix:
            row.append(float('inf'))
        self.adjacency_matrix.append(new_row)
        # edge from node to itself is 0
        self.set_edge_weighted(node, node, 0)

    def set_edge_weighted(self, node1, node2, weight):
        # get the index of each node
        index1 = self.get_node_via_row_column(node1.row, node1.column).get_index()
        index2 = self.get_node_via_row_column(node2.row, node2.column).get_index()
        # set the edge in the adjacency matrix
        self.adjacency_matrix[index1][index2] = weight
        self.adjacency_matrix[index2][index1] = weight
        # update the number of edges
        self.number_of_edges += 1

    def set_edge_unweighted(self, node1, node2):
        # get the index of each node
        index1 = self.get_node_via_row_column(node1.row, node1.column).get_index()
        index2 = self.get_node_via_row_column(node2.row, node2.column).get_index()
        # set the edge in the adjacency matrix
        self.adjacency_matrix[index1][index2] = 1
        self.adjacency_matrix[index2][index1] = 1
        # update the number of edges
        self.number_of_edges += 1

    def get_node_via_row_column(self, row, column):
        return self.nodesDictionary.get((row, column))

    def get_edge(self, node1, node2):
        index1 = self.get_node_via_row_column(node1.row, node1.column).get_index()
        index2 = self.get_node_via_row_column(node2.row, node2.column).get_index()
        return self.adjacency_matrix[index1][index2]

    def get_edge_via_index(self, node_1_index, node_2_index):
        return self.adjacency_matrix[node_1_index][node_2_index]

    def get_node_via_index(self, index):
        return self.nodeIndices.get(index)

    def get_node_via_name(self, name):
        return self.nodeNames.get(name)

    def print_adjacency_matrix(self):
        print("\nAdjacency Matrix:")
        for row in self.adjacency_matrix:
            print(row)

    def print_adjacency_list(self):
        print("\nAdjacency List:")
        for node in self.nodesDictionary.values():
            print(node.get_name(), end=": ")
            for neighbor in node.get_neighbors(self):
                print(neighbor.get_name(), end=" ")
            print()
