class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.number_of_edges = 0
        # Initialize as an empty list
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
        self.nodesDictionary[(node.x, node.y)] = node
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
        index1 = self.get_node_via_xy(node1.x, node1.y).get_index()
        index2 = self.get_node_via_xy(node2.x, node2.y).get_index()
        # set the edge in the adjacency matrix
        self.adjacency_matrix[index1][index2] = weight
        self.adjacency_matrix[index2][index1] = weight
        # update the number of edges
        self.number_of_edges += 1

    def set_edge_unweighted(self, node1, node2):
        # get the index of each node
        index1 = self.get_node_via_xy(node1.x, node1.y).get_index()
        index2 = self.get_node_via_xy(node2.x, node2.y).get_index()
        # set the edge in the adjacency matrix
        self.adjacency_matrix[index1][index2] = 1
        self.adjacency_matrix[index2][index1] = 1
        # update the number of edges
        self.number_of_edges += 1

    def get_node_via_xy(self, x, y):
        return self.nodesDictionary.get((x, y))

    def get_edge(self, node1, node2):
        index1 = self.get_node_via_xy(node1.x, node1.y).get_index()
        index2 = self.get_node_via_xy(node2.x, node2.y).get_index()
        return self.adjacency_matrix[index1][index2]

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


def maze_to_graph_coords(maze_row, maze_column, total_rows):
    graph_x = maze_column
    graph_y = total_rows - maze_row + 1
    return graph_x, graph_y


def graph_to_maze_coords(graph_x, graph_y, total_rows):
    maze_row = total_rows - graph_y + 1
    maze_column = graph_x
    return maze_row, maze_column
