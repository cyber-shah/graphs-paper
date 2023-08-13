import heapq


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
    source_node = graph.get_node_via_index(source_index)

    # Initialize the priority queue and distance list ______________________________________
    priority_queue = [(0, source_index)]  # (distance, node_index)
    visited_list = [False] * total_nodes
    # distance list init
    distance_list = [float('inf')] * total_nodes
    for neighbor in source_node.get_neighbors(graph):
        neighbor_index = neighbor.get_index()
        distance_list[neighbor_index] = graph.get_edge(source_node, neighbor)
        heapq.heappush(priority_queue, (distance_list[neighbor_index], neighbor_index))
    distance_list[source_index] = 0

    explored_nodes_indexes = []
    previous_nodes = [-1] * total_nodes

    # DIJKSTRA starts here ________________________________________________________________
    while priority_queue:
        # Extract the node with the minimum distance from the priority queue
        current_distance, current_node_index = heapq.heappop(priority_queue)
        explored_nodes_indexes.append(current_node_index)
        current_node = graph.get_node_via_index(current_node_index)
        visited_list[current_node_index] = True

        # If the destination node is visited, we can stop the algorithm
        if current_node_index == destination_index:
            break

        # 2. Loop over all of its adjacent nodes.
        for neighbour in current_node.get_neighbors(graph):
            neighbour_index = neighbour.get_index()
            edge_weight = graph.get_edge(current_node, neighbour)
            new_distance = distance_list[current_node_index] + edge_weight
            neighbor_distance = distance_list[neighbour_index]

            # 2.1 Relax all adjacent unvisited nodes.
            if visited_list[neighbour_index] is False and neighbour_index != source_index:
                if new_distance < neighbor_distance:
                    # 2.2 If the new distance is less than the current distance, update the distance.
                    heapq.heappush(priority_queue, (new_distance, neighbour_index))
                    previous_nodes[neighbour_index] = current_node_index
                    distance_list[neighbour_index] = new_distance

    shortest_path = []
    current_node = destination_index
    while current_node != -1:
        shortest_path.insert(0, current_node)
        current_node = previous_nodes[current_node]

    return explored_nodes_indexes, shortest_path
