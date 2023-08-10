from model import Node as Node, Graph
import networkx as nx
import matplotlib.pyplot as plt

from algorithms import Dijkstra, BFS


def create_grid_graph():
    graph = Graph.Graph()

    # create Nodes and add them to the graph
    for x in range(20):
        for y in range(20):
            name = "(" + str(x) + ", " + str(y) + ")"
            graph.add_node(Node.Node(name, x, y))

    # create edges
    for x in range(20):
        for y in range(20):
            if x > 0:
                graph.set_edge_unweighted(graph.get_node_via_xy(x, y), graph.get_node_via_xy(x - 1, y))
            if y > 0:
                graph.set_edge_unweighted(graph.get_node_via_xy(x, y), graph.get_node_via_xy(x, y - 1))
            if x < 19:
                graph.set_edge_unweighted(graph.get_node_via_xy(x, y), graph.get_node_via_xy(x + 1, y))
            if y < 19:
                graph.set_edge_unweighted(graph.get_node_via_xy(x, y), graph.get_node_via_xy(x, y + 1))

    return graph
    # print adjacency matrix
    # graph.print_adjacency_matrix()

    # print adjacency list
    # graph.print_adjacency_list()


def plot_graph(graph):
    nx_graph = nx.Graph()

    # Add nodes
    for node in graph.nodesDictionary.values():
        nx_graph.add_node(node.get_index())

    # Add edges
    # for i in range(graph.number_of_nodes):
    #     for j in range(i + 1, graph.number_of_nodes):
    #         if graph.adjacency_matrix[i][j] != float('inf'):
    #             nx_graph.add_edge(i, j)

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


def draw_graph(graph, nx_graph, pos, exploration_history_indexes, shortest_path_indexes):
    # Draw the graph in grid layout
    nx.draw(nx_graph, pos, with_labels=True, node_size=50, node_color='black', font_size=4)

    # Highlight explored nodes
    nx.draw_networkx_nodes(nx_graph, pos, nodelist=exploration_history_indexes,
                           node_color='yellow', node_size=50)

    # Highlight the shortest path
    shortest_path_edges = [(shortest_path_indexes[i], shortest_path_indexes[i + 1])
                           for i in range(len(shortest_path_indexes) - 1)]
    nx.draw_networkx_edges(nx_graph, pos, edgelist=shortest_path_edges, edge_color='red', width=2)

    plt.show()


def main():
    graph = create_grid_graph()

    nx_graph, pos = plot_graph(graph)

    start_node_name = graph.get_node_via_xy(2, 4).name
    end_node_name = graph.get_node_via_xy(8, 8).name
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
