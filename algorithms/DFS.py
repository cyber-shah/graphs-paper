from collections import deque


def dfs(graph, source_node_name):
    source_node_index = graph.get_node_index(source_node_name)

    stack = deque()
    visited = [False] * len(graph.number_of_nodes)
    distances_list = []
    visited_count = 0

    visited[source_node_index] = True
    stack.append(source_node_index)
    distances_list.append(source_node_index)

    while stack:
        current_node_index = stack.pop()

        for i in range(len(graph.nodes)):
            if graph.adjacency_matrix[current_node_index][i] != float('inf') and not visited[i]:
                visited[i] = True
                stack.append(i)
                visited_count += 1
                distances_list.append(i)

    return distances_list


def dfs_destination(graph, source_node_name, destination_node_name):
    # getters ________________________________________________________
    source_node_index = (graph.get_node_via_name
                         (source_node_name).index)
    destination_node_index = (graph.get_node_via_name
                              (destination_node_name).index)

    # initialize ______________________________________________________
    stack = deque()
    visited = [False] * graph.number_of_nodes
    distances_list = []  # to store the order of visited nodes
    parent_map = {}  # To store parent nodes for backtracking

    visited[source_node_index] = True
    stack.append(source_node_index)
    distances_list.append(source_node_index)

    while stack:
        current_node_index = stack.pop()

        if current_node_index == destination_node_index:
            break

        for i in range(graph.number_of_nodes):
            if graph.adjacency_matrix[current_node_index][i] != float('inf') and not visited[i]:
                visited[i] = True
                stack.append(i)
                distances_list.append(i)
                parent_map[i] = current_node_index  # Store parent information

    if destination_node_index not in parent_map:
        return distances_list, []

    shortest_path = build_shortest_path(parent_map, source_node_index, destination_node_index)
    return distances_list, shortest_path


def build_shortest_path(parent_map, source_node_index, destination_node_index):
    current_node_index = destination_node_index
    shortest_path = []

    while current_node_index != source_node_index:
        shortest_path.append(current_node_index)
        current_node_index = parent_map[current_node_index]

    shortest_path.append(source_node_index)
    shortest_path.reverse()
    return shortest_path
