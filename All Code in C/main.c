#include <stdio.h>
#include <stdlib.h>

#include "algorithms/djikstra.h"


int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <vertices_path> <distances_path>\n", argv[0]);
        return 1;
    }

    // get the file path
    char *filepath_1 = argv[1];
    char *filepath_2 = argv[2];

    // initialize graph and create vertices
    Graph *graph = graph_from_file(filepath_1, filepath_2);

    // print the graph
    print_graph(graph);

    // get the source node
    char sourceName[100];
    printf("\n\nEnter the source node: ");
    scanf("%s", sourceName);
    int sourceNodeIndex = get_index(graph, sourceName);
    if (sourceNodeIndex == -1) {
        printf("Node not found.\n");
        return 1;
    }

    // get the shortest path list
    int* shortest_path_list = Dijkstra(sourceNodeIndex, graph, true);

    free(shortest_path_list);

    return 0;
}