//
// Created by shahp on 8/7/2023.
//


#include "algorithms/djikstra.h"


int test_graphs() {
    char* stringVertices = "a\nb\nc\nd";
    char* stringDistances = "a b 2\nb c 1\na c 4\nc d 2\na d 8";

    Graph *graph = graph_from_string(stringVertices, stringDistances);

    free_graph(graph);
    return 1;
}


int test_djikstra() {
    char* stringVertices = "a\nb\nc\nd";
    char* stringDistances = "a b 2\nb c 1\na c 4\nc d 2\na d 8";

    Graph *graph = graph_from_string(stringVertices, stringDistances);
    int* shortest_path_list = Dijkstra(0, graph, true);

    if (shortest_path_list[0] != 0) {
        printf("shortest_path_list from source to source must be 0\n");
        return 0;
    } else if (shortest_path_list[1] != 2) {
        printf("shortest_path_list from source to B must be 2\n");
        return 0;
    } else if (shortest_path_list[2] != 3) {
        printf("shortest_path_list from source to C must be 3\n");
        return 0;
    } else if (shortest_path_list[3] != 5) {
        printf("shortest_path_list from source to D must be 5\n");
        return 0;
    }

    free_graph(graph);
    free(shortest_path_list);
    return 1;
}


int (*unitTests[])(int) = {
        test_graphs,
        test_djikstra,
};



/** use this file for tests.
 *
 * Below isn't actually any 'real' tests, it
 * just simply is a sample run.
*/
int main() {
    // TESTING SUITE ----------------------------------
    unsigned int testsPassed = 0;
    // List of Unit Tests to test your data structure
    int counter = 0;
    while (unitTests[counter] != NULL)
    {
        printf("\n\n========unitTest %d========\n", counter);
        if (1 == unitTests[counter](1))
        {
            printf("passed test\n");
            testsPassed++;
        }
        else
        {
            printf("failed test, missing functionality, or incorrect test\n");
        }
        counter++;
    }

    printf("%d of %d tests passed\n", testsPassed, counter);


    return 0;
}