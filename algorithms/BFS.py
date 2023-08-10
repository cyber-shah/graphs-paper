from collections import deque


def bfs_destination(graph, source_node_name, destination_node_name):
    """
    This function performs BFS on the graph and returns the order of explored nodes and shortest path from source node
    Pseudo code:
    1. Initialize a queue and a visited array
    2. Mark the source node as visited and enqueue it
    3. While queue is not empty
        3.1. Dequeue a node from the queue
        3.2. If the dequeued node is the destination node, break the loop
        3.3. Else visit all the adjacent nodes of current node
            3.3.1. Enqueue all the unvisited adjacent nodes and mark them as visited
    4. Repeat step 3 until queue is empty

    :param graph: Graph object
    :param source_node_name: Name of the source node
    :param destination_node_name: Name of the destination node
    :return: order of visited nodes and shortest path from source to destination
    """
    # Getters ________________________________________________________
    source_node_index = graph.get_node_via_name(source_node_name).index
    destination_node_index = graph.get_node_via_name(destination_node_name).index

    # Initialize ______________________________________________________
    queue = deque()
    visited = [False] * graph.number_of_nodes
    explored_nodes_indices = []  # To store the order of visited nodes
    parent_map = {}  # To store parent nodes for backtracking

    visited[source_node_index] = True
    queue.append(source_node_index)
    explored_nodes_indices.append(source_node_index)

    # While queue is not empty _________________________________________
    while queue:
        current_node_index = queue.popleft()

        # if destination node is found, break the loop
        if current_node_index == destination_node_index:
            break

        # else visit all the adjacent nodes of current node
        # append them to the queue and mark them as visited
        for i in range(graph.number_of_nodes):
            if graph.adjacency_matrix[current_node_index][i] != float('inf') and not visited[i]:
                visited[i] = True
                queue.append(i)
                explored_nodes_indices.append(i)
                parent_map[i] = current_node_index  # Store parent information

    # If destination node is not found, return shortest path as empty list
    if destination_node_index not in parent_map:
        return explored_nodes_indices, []

    # Else build the shortest path and return it
    shortest_path = build_shortest_path(parent_map, source_node_index, destination_node_index)
    return explored_nodes_indices, shortest_path


def build_shortest_path(parent_map, source_node_index, destination_node_index):
    """
    This function builds the shortest path from source node to destination node

    :param parent_map: Dictionary containing parent information
    :param source_node_index: index of the source node
    :param destination_node_index: index of the destination node
    :return: shortest_path from source node to destination node
    """
    current_node_index = destination_node_index
    shortest_path = []

    while current_node_index != source_node_index:
        shortest_path.append(current_node_index)
        current_node_index = parent_map[current_node_index]

    shortest_path.append(source_node_index)
    shortest_path.reverse()
    return shortest_path
