import networkx as nx

import model.Graph as GraphRC
import model.Node as NodeRC
from view.lib.pyaMaze.pyamaze.pyamaze import maze

# global variables
maze_row_size = 100
maze_col_size = 100
goal_row = 100
goal_col = 100
loop_percent = 10
maze_save_file = 'maze-10-size-100'


class DatasetGenerator:
    def __init__(self):
        self.graph = None

    def create_maze(self):
        custom_maze = maze(maze_row_size, maze_col_size)
        custom_maze.CreateMaze(goal_row, goal_col,
                               loopPercent=loop_percent, saveMaze=True)
        custom_maze.run()

    def create_grid_graph(self):
        graph = GraphRC.GraphRC()

        # create Nodes and add them to the graph
        for x in range(maze_col_size):
            for y in range(maze_row_size):
                name = "(" + str(x) + ", " + str(y) + ")"
                graph.add_node(NodeRC.NodeRC(name, x, y))

        # create edges
        for x in range(maze_col_size):
            for y in range(maze_row_size):
                if x > 0:
                    graph.set_edge_unweighted(graph.get_node_via_row_column
                                              (x, y), graph.get_node_via_row_column(x - 1, y))
                if y > 0:
                    graph.set_edge_unweighted(graph.get_node_via_row_column
                                              (x, y), graph.get_node_via_row_column(x, y - 1))
                if x < maze_col_size - 1:
                    graph.set_edge_unweighted(graph.get_node_via_row_column
                                              (x, y), graph.get_node_via_row_column(x + 1, y))
                if y < maze_row_size - 1:
                    graph.set_edge_unweighted(graph.get_node_via_row_column
                                              (x, y), graph.get_node_via_row_column(x, y + 1))

        return self.plot_graph(graph)

    def plot_graph(self, graph):
        """
        Converts the graph to a networkx graph and plots it
        :param graph:  the graph to plot
        :return:  the plotted graph
        """
        nx_graph = nx.Graph()

        # Add nodes
        for node in graph.nodesDictionary.values():
            nx_graph.add_node(node.get_index())

        # Add edges
        for i in range(graph.number_of_nodes):
            for j in range(i + 1, graph.number_of_nodes):
                if graph.adjacency_matrix[i][j] != float('inf'):
                    nx_graph.add_edge(i, j)

        # Create a grid layout for the nodes
        grid_size = int(graph.number_of_nodes ** 0.5)
        grid_spacing = 1.0  # Adjust this to control the spacing between nodes

        # Calculate positions for the nodes
        pos = {}
        for i in range(graph.number_of_nodes):
            row = i // grid_size
            col = i % grid_size
            pos[i] = (col * grid_spacing, row * grid_spacing)

        return nx_graph, pos


def main():
    # to save a maze, uncomment the following line
    DatasetGenerator().create_maze()

    # to save a grid graph, uncomment the following line
    # nx_graph, pos = DatasetGenerator().create_grid_graph()


if __name__ == '__main__':
    main()
