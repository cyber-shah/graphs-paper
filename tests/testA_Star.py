from model.Graph import GraphRC as Graph
from model.Node import NodeRC as Node
from algorithms import A_star as a_star


def test_a_star_destination():
    # create a graph
    graph = Graph()

    # create nodes
    node_a = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")
    node_e = Node("E")
    node_f = Node("F")
    node_g = Node("G")
    node_h = Node("H")

    # add nodes to the graph
    graph.add_node(node_a)
    graph.add_node(node_b)
    graph.add_node(node_c)
    graph.add_node(node_d)
    graph.add_node(node_e)
    graph.add_node(node_f)
    graph.add_node(node_g)
    graph.add_node(node_h)

    # add edges to the graph
    graph.set_edge_weighted(node_a, node_b, 4)
    graph.set_edge_weighted(node_a, node_c, 2)
    graph.set_edge_weighted(node_b, node_c, 1)
    graph.set_edge_weighted(node_b, node_d, 5)
    graph.set_edge_weighted(node_c, node_d, 8)
    graph.set_edge_weighted(node_c, node_e, 10)
    graph.set_edge_weighted(node_d, node_e, 2)
    graph.set_edge_weighted(node_d, node_f, 6)
    graph.set_edge_weighted(node_e, node_f, 2)
    graph.set_edge_weighted(node_e, node_g, 5)
    graph.set_edge_weighted(node_f, node_g, 1)
    graph.set_edge_weighted(node_f, node_h, 3)
    graph.set_edge_weighted(node_g, node_h, 9)

    # test shortest path from A to H
    explored_nodes_indices, path = a_star.a_star_destination(graph, "A", "H")
    assert explored_nodes_indices == [0, 2, 1, 3, 4, 5, 6, 7]
    assert path == [0, 2, 1, 3, 5, 6, 7]

    # test shortest path from B to G
    explored_nodes_indices, path = a_star.a_star_destination(graph, "B", "G")
    assert explored_nodes_indices == [1, 2, 0, 3, 4, 5, 6]
    assert path == [1, 2, 3, 5, 6]

    # test shortest path from C to F
    explored_nodes_indices, path = a_star.a_star_destination(graph, "C", "F")
    assert explored_nodes_indices == [2, 1, 3, 4, 5]
    assert path == [2, 1, 3, 5, 4]

    # test shortest path from D to E
    explored_nodes_indices, path = a_star.a_star_destination(graph, "D", "E")
    assert explored_nodes_indices == [3, 4]
    assert path == [3, 5, 4]

    # test shortest path from E to A
    explored_nodes_indices, path = a_star.a_star_destination(graph, "E", "A")
    assert explored_nodes_indices == [4, 5, 6, 7, 2, 1, 0]
    assert path == []

if __name__ == '__main__':
    test_a_star_destination()