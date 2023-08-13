import heapq


def a_star_destination(graph, source_node_name, destination_node_name):
    """
    there's two ways algorithm can be completed
    1. destination node is found
    2. open_unvisited_set is empty - no path to destination node

    closed set starts as empty set, and then just grows
    start with only the source node in it and then add nodes to it as we visit them

    psuedocode:
    1. Create an open_unvisited_set (priority queue) to store nodes to be explored.
    2. Create a closed_visited_set (set) to store nodes that have been visited.
    3. Add the starting node to the open_unvisited_set.
    4. while the open_unvisited_set is not empty
        a. Get the current node from the open_unvisited_set with the lowest f_score.
        b. Remove the current node from the open_unvisited_set and add it to the closed_visited_set.
        c. If the current node is the destination node, terminate the loop.
        d. Else, for each neighbor of the current node:
            i. Calculate tentative_g = current_node_index.g + distance from current node to neighbor
            ii. If neighbor in closed_visited_set and the tentative_g > neighbor.g
                1. skip this iteration.
            iii. If the neighbor not in open_unvisited_set or tentative_g_score < neighbor.g:
                1. Set neighbor.g = tentative_g (update neighbor.g)
                2. Set neighbor.h = distance from neighbor to destination node (update heuristic)
                3. Set neighbor.f = neighbor.g + neighbor.h (update neighbor.f)
                4. Set neighbor.parent = current_node_index (update parent)
                5. If neighbor not in open_unvisited_set:
                    a. Add neighbor to open_unvisited_set.
    5. Once the loop terminates:
        a. If the destination node has been visited:
            i. reconstruct the path from destination node to source node using parent pointers.
        b. Else:
            i. No path exists from source node to destination node.
    """
    # instantiate ____________________________________________________
    open_unvisited_set = []  # unvisited nodes
    closed_visited_set = set()  # visited nodes
    explored_nodes_indices = []  # explored nodes

    # Getters ________________________________________________________
    source_node_index = graph.get_node_via_name(source_node_name).index
    destination_node_index = graph.get_node_via_name(destination_node_name).index
    source_node = graph.get_node_via_index(source_node_index)
    destination_node = graph.get_node_via_index(destination_node_index)

    # Setters ______________________________________________________
    source_node.g = 0
    source_node.h = heuristic(source_node, destination_node)
    source_node.f = source_node.g + source_node.h
    heapq.heappush(open_unvisited_set, (source_node.f, source_node))

    # while there are unvisited nodes
    while open_unvisited_set:
        # set operations ____________________________________________
        # get the current node from the open_unvisited_set
        # with the lowest f_score
        f, current_node = heapq.heappop(open_unvisited_set)
        if current_node in closed_visited_set:
            continue
        closed_visited_set.add(current_node)
        explored_nodes_indices.append(current_node.index)

        # if destination node is found ______________________________
        if current_node.index == destination_node.index:
            break

        # for all neighbors _________________________________________
        # else visit all the UNVISITED adjacent nodes of current node
        for neighbor in current_node.get_neighbors(graph):
            # calculate tentative_g
            tentative_g = current_node.g + graph.get_edge(current_node, neighbor)

            # if neighbor is visited and the tentative_g > neighbor.g,
            # we already have a better path
            if neighbor in closed_visited_set and tentative_g >= neighbor.g:
                continue

            # if the neighbor is not already visited or
            # the tentative_g is less than the neighbor.g
            if neighbor not in open_unvisited_set or tentative_g < neighbor.g:
                # update all the values of neighbour to this new path
                neighbor.g = tentative_g
                neighbor.h = heuristic(neighbor, destination_node)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.parent = current_node

                # if neighbour is not in the unvisited set, add it to visit again
                if neighbor not in open_unvisited_set:
                    heapq.heappush(open_unvisited_set, (neighbor.f, neighbor))

    # return the path
    path = []
    current = destination_node
    while current is not None:
        path.append(current.index)
        current = current.parent
    return explored_nodes_indices, path[::-1]


def heuristic(source_node, goal_node):

    return abs(source_node.row - goal_node.row) + abs(source_node.column - goal_node.column)
