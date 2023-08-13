#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include "graph.h"

void print_shortest_path(int* distances_list, int sourceNode, Graph* graph);
int find_min_distance_node(const bool visited_list[], const int distances_list[], int totalNodes);

/**
 * This function is the implementation of the Dijkstra algorithm.
 * here distance = sum of weights of edges from source node to the current node.
 *                  or the distance from the source node to the current node.
 * 1. find the node with the minimum distance to visit next.
 * 2. Loop over all of its adjacent nodes.
 *      2.1 Relax all the adjacent nodes unvisited nodes. (why?)
 *              because we visit a node only when we have found the shortest path to it 
 *              and there is no other shorter path.
 *      2.2 If the new distance is less than the current distance, update the distance.
 * 3. Pick the smallest distance node from unvisited nodes.
 * 4. Repeat steps 2 and 3 until all the nodes are visited_list.
 * 5. Keep updating the distance array.
 * 
 * @param sourceNode the source node.
 * @param graph the graph to find the shortest path.
 * @returns distances_list an array of distances from the source node to all the nodes.
*/
int* Dijkstra(int sourceNode, Graph *graph, bool print) {
    
    int totalNodes = graph->numberOfNodes;
    
    // initialize all the visited_list nodes to false.
    bool* visited_list = (bool*) malloc(sizeof(bool) * totalNodes);
    // array of nodes - to store the distance from the source node.
    int* distances_list = (int*) malloc(sizeof(int) * totalNodes);


    // initialize the distances array and visited array.
    // They all mean from the source Node.
    for (int i = 0; i < totalNodes; i++) {
        // if the distance is not INF, then it is the distance.
        if (graph->adjacencyMatrix[sourceNode][i] != INF) {
            distances_list[i] = graph->adjacencyMatrix[sourceNode][i];
        } else {
            distances_list[i] = INF;
        }
        visited_list[i] = false;
    }
    // distance of source node from itself is 0.
    distances_list[sourceNode] = 0;

    // loop through all the nodes
    for (int i = 0; i < (totalNodes - 1); ++i) {
        // finds the node with the minimum distance to visit next.
        int minDistanceNode = find_min_distance_node(visited_list, distances_list, totalNodes);

        // mark the node as visited
        visited_list[minDistanceNode] = true;

        // loop through all the nodes.
        for (int j = 0; j < totalNodes; ++j) {
            // relax all the adjacent unvisited nodes. adjacent means distance != INF
            if (visited_list[j] == false && graph->adjacencyMatrix[minDistanceNode][j] != INF && graph->adjacencyMatrix[minDistanceNode][j] != 0) {
                int newDistance = distances_list [minDistanceNode] 
                                  + graph->adjacencyMatrix[minDistanceNode][j];
                if (newDistance < distances_list[j]) {
                    // update the distance
                    distances_list[j] = newDistance;
                }
            }
        }
    }
    free(visited_list);

    if (print == true) {
        print_shortest_path(distances_list, sourceNode, graph);
    }

    return distances_list;
}

/**
 * Finds the unvisited node with the minimum distance.
 *
 * @param visited_list the array of visited_list nodes.
 * @param distArray the array of nodes with their distance from the source node.
 * @returns node_index with the minimum distance.
*/
int find_min_distance_node(const bool visited_list[], const int distances_list[], int totalNodes) {
    int minDistance = INF;
    int node_index = -1;

    // for all nodes if unvisited and distance less than minDistance.
    for (int i = 0; i < totalNodes; i++) {
        if (visited_list[i] == false && distances_list[i] <= minDistance && distances_list[i] != 0) {
            minDistance = distances_list[i];
            node_index = i;
        }
    }
    return node_index;
}

/**
 * Prints the shortest path from the source node to all the nodes.
 *
 * @param distances_list output from the Dijkstra algorithm.
 * @param sourceNode the source node.
 * @param graph the graph to print the shortest path.
 */
void print_shortest_path(int* distances_list, int sourceNode, Graph* graph) {
    printf("Shortest path from node %s:\n\n", graph->nodes[sourceNode]->name);

    for (int i = 0; i < graph->numberOfNodes; i++) {
        if (distances_list[i] == INF) {
            printf("%s is not reachable.\n", graph->nodes[i]->name);
        } else {
            printf("%s is %d units away.\n",
                   graph->nodes[i]->name,
                   distances_list[i]);
        }
    }
}
