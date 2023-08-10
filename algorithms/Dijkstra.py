def dijkstra(graph, source_node_name):
    """
    This function is the implementation of the Dijkstra algorithm.
    here distance = sum of weights of edges from source node to the current node.

    1. find the node with the minimum distance to visit next.
    2. Loop over all of its adjacent nodes.
        2.1 Relax all adjacent unvisited nodes. WHY?
            because we visit a node only when we have found the shortest path to it
            and there is no other shorter path.
        2.2 If the new distance is less than the current distance, update the distance.
    3. Repeat steps 1 and 2 until all the nodes are visited.
    """
    # get total and index of source node ____________________________________________
    total_nodes = graph.number_of_nodes
    source_index = graph.get_node_via_name(source_node_name).get_index()

    # Initialize the visited and distance list _______________________________________
    visited_list = [False] * total_nodes

    distance_list = [float('inf')] * total_nodes
    distance_list[source_index] = 0
    # init the distance list by copying the weights from the graph
    # all distances are from the source node
    for i in range(total_nodes):
        source_node = graph.get_node_via_index(source_index)
        destination_node = graph.get_node_via_index(i)
        if i != source_index and graph.get_edge(source_node, destination_node) != float('inf'):
            distance_list[i] = graph.get_edge(source_node, destination_node)

    # DIJKSTRA starts here ________________________________________________________________
    for i in range(total_nodes):
        # 1. find the node with the minimum distance to visit next.
        min_distance_node = get_min_distance_node(visited_list, distance_list)
        # Mark the node as visited
        visited_list[min_distance_node] = True

        # 2. Loop over all of its adjacent nodes.
        for j in range(total_nodes):
            source_node = graph.get_node_via_index(min_distance_node)
            destination_node = graph.get_node_via_index(j)
            edge_weight = graph.get_edge(source_node, destination_node)
            # 2.1 Relax all adjacent unvisited nodes.
            if not visited_list[j] and edge_weight != float('inf'):
                # 2.2 If the new distance is less than the current distance, update the distance.
                if distance_list[min_distance_node] + edge_weight < distance_list[j]:
                    distance_list[j] = distance_list[min_distance_node] + edge_weight

    return distance_list


def dijkstra_path(graph, source_node_name, destination_node_name):
    """
    This function is the implementation of the Dijkstra algorithm.
    here distance = sum of weights of edges from source node to the current node.

    1. find the node with the minimum distance to visit next.
    2. Loop over all of its adjacent nodes.
        2.1 Relax all adjacent unvisited nodes. WHY?
            because we visit a node only when we have found the shortest path to it
            and there is no other shorter path.
        2.2 If the new distance is less than the current distance, update the distance.
    3. Repeat steps 1 and 2 until all the nodes are visited.
    """
    # get total and index of source node ____________________________________________
    total_nodes = graph.number_of_nodes
    source_index = graph.get_node_via_name(source_node_name).get_index()
    destination_index = graph.get_node_via_name(destination_node_name).get_index()

    # Initialize the visited and distance list _______________________________________
    visited_list = [False] * total_nodes

    distance_list = [float('inf')] * total_nodes
    distance_list[source_index] = 0
    # init the distance list by copying the weights from the graph
    # all distances are from the source node
    for i in range(total_nodes):
        source_node = graph.get_node_via_index(source_index)
        destination_node = graph.get_node_via_index(i)
        if i != source_index and graph.get_edge(source_node, destination_node) != float('inf'):
            distance_list[i] = graph.get_edge(source_node, destination_node)

    # for getting the path and explored nodes ____________________________________________
    explored_nodes_indexes = []
    previous_nodes = [-1] * total_nodes  # Initialize with -1, meaning no previous node

    # DIJKSTRA starts here ________________________________________________________________
    for i in range(total_nodes):
        # 1. find the node with the minimum distance to visit next.
        min_distance_node = get_min_distance_node(visited_list, distance_list)
        # Mark the node as visited
        visited_list[min_distance_node] = True
        explored_nodes_indexes.append(min_distance_node)

        # If the destination node is visited, we can stop the algorithm
        if min_distance_node == destination_index:
            break

        # 2. Loop over all of its adjacent nodes.
        # TODO : change this to neighbours instead of all nodes
        for j in range(total_nodes):
            source_node = graph.get_node_via_index(min_distance_node)
            destination_node = graph.get_node_via_index(j)
            edge_weight = graph.get_edge(source_node, destination_node)
            # 2.1 Relax all adjacent unvisited nodes.
            if not visited_list[j] and edge_weight != float('inf'):
                # 2.2 If the new distance is less than the current distance, update the distance.
                if distance_list[min_distance_node] + edge_weight < distance_list[j]:
                    distance_list[j] = distance_list[min_distance_node] + edge_weight
                    previous_nodes[j] = min_distance_node

    # Backtrack to construct the shortest path ____________________________________________
    shortest_path = []
    current_node = destination_index
    while current_node != -1:
        shortest_path.insert(0, current_node)
        current_node = previous_nodes[current_node]

    return distance_list, explored_nodes_indexes, shortest_path


def get_min_distance_node(visited_list, distance_list):
    """
    This function returns the node with the minimum distance to visit next.

    @param visited_list: list of booleans, True if the node is visited, False otherwise.
    @param distance_list: list of floats, the distance from the source node to the current node.
    @return: the index of the node with the minimum distance to visit next.
    """
    min_distance = float('inf')
    min_distance_node = None
    for i in range(len(distance_list)):
        # if not visited and distance is less than the current min distance
        if not visited_list[i] and distance_list[i] < min_distance:
            min_distance = distance_list[i]
            min_distance_node = i
    return min_distance_node
