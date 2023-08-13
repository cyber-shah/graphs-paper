from model import Node as Node, Graph
from model import Node as NodeRC, Graph as GraphRC
import networkx as nx
import matplotlib.pyplot as plt

from algorithms import Dijkstra, BFS

# global variables
x_size = 20
y_size = 20

def create_grid_graph():
    graph = GraphRC.GraphRC()

    # create Nodes and add them to the graph
    for x in range(x_size):
        for y in range(y_size):
            name = "(" + str(x) + ", " + str(y) + ")"
            graph.add_node(NodeRC.NodeRC(name, x, y))

    # create edges
    for x in range(x_size):
        for y in range(y_size):
            if x > 0:
                graph.set_edge_unweighted(graph.get_node_via_row_column(x, y), graph.get_node_via_row_column(x - 1, y))
            if y > 0:
                graph.set_edge_unweighted(graph.get_node_via_row_column(x, y), graph.get_node_via_row_column(x, y - 1))
            if x < x_size - 1:
                graph.set_edge_unweighted(graph.get_node_via_row_column(x, y), graph.get_node_via_row_column(x + 1, y))
            if y < y_size - 1:
                graph.set_edge_unweighted(graph.get_node_via_row_column(x, y), graph.get_node_via_row_column(x, y + 1))

    return graph


def plot_graph(graph):
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
    graph = create_grid_graph()

    nx_graph, pos = plot_graph(graph)

    start_node_name = graph.get_node_via_row_column(2, 4).name
    end_node_name = graph.get_node_via_row_column(8, 8).name
    distances_list, exploration_history_indexes, shortest_path_indexes = (
        Dijkstra.dijkstra_path(graph, start_node_name, end_node_name))

    exploration_history_indexes, shortest_path_indexes = (
        BFS.bfs_destination(graph, start_node_name, end_node_name))

    draw_graph(graph, nx_graph, pos, exploration_history_indexes, shortest_path_indexes)

#     # Initialize the plot with the initial state
#     draw_graph(graph, nx_graph, pos, [], [])
#
#     fig, ax = plt.subplots()
#
#     animation = FuncAnimation(
#         fig, update_plot,
#         fargs=(graph, nx_graph, pos, exploration_history_indexes, shortest_path_indexes),
#         frames=range(100),  # Adjust max_iterations as needed
#         repeat=False
#     )
#
#     plt.show()
#
#
# def update_plot(frame, graph, nx_graph, pos, exploration_history, shortest_path):
#     # Perform a single step of the algorithm
#     exploration_history_slice = exploration_history[:frame + 1]
#     shortest_path_slice = shortest_path[:frame + 1]
#
#     # Clear the current plot
#     plt.clf()
#
#     # Plot the graph and the updated exploration_history and shortest_path
#     draw_graph(graph, nx_graph, pos, exploration_history_slice, shortest_path_slice)


if __name__ == "__main__":
    main()
