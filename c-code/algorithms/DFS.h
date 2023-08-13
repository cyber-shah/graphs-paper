
#include "graph.h"
#include "mystack.h"

/**
 * This is a recursive helper function for DFS.
 * It calls itself until
 * @param graph
 * @param sourceNodeIndex
 * @param visited
 */
void dfsHelper(Graph *graph, int sourceNodeIndex, bool visited[]) {
    // base case - set the node to visited
    visited[sourceNodeIndex] = true;

    // recursive case - if there is an adjacent node that is not visited, then visit it
    for (int i = 0; i < graph->numberOfNodes; ++i) {
        if (graph->adjacencyMatrix[sourceNodeIndex][i] != INF && !visited[i]) {
            dfsHelper(graph, i, visited);
        }
    }
}

/**
 * Psuedo code for DFS:
 *
 * @param graph
 * @param sourceNodeIndex
 */
void dfs_recursive(Graph *graph, int sourceNodeIndex) {
    bool visited[MAX_NODES] = {false};
    dfsHelper(graph, sourceNodeIndex, visited);
}


/**
 * Psuedo code for DFS:
 * 1. Create a stack
 * 2. Push the source node
 * 3. While stack is not empty
 *     3.1 Pop the top node
 *     3.2 if the node is not visited
 *             1 mark the node as visited
 *             2 push all the adjacent nodes of the current node
 *               that are not visited
 *             3 repeat 3.1 and 3.2
 * @param graph
 * @param sourceNodeIndex
 */
int* dfs(Graph *graph, int sourceNodeIndex) {
    // create a stack for DFS
    bool visited[MAX_NODES] = {false};
    neu_stack* stack = create_stack(graph->numberOfNodes);
    int* distances_list = (int*) malloc(sizeof(int) * graph->numberOfNodes);
    int visited_count = 0; // to keep track of the number of visited nodes

    // mark the source node as visited
    visited[sourceNodeIndex] = true;
    stack_push(stack, sourceNodeIndex);
    distances_list[visited_count] = sourceNodeIndex; // Add source node to the list

    // loop until stack is empty
    while (!stack_empty(stack)) {
        // pop the top node
        int currentNodeIndex = stack_pop(stack);
        printf("%s ", graph->nodes[currentNodeIndex]->name);

        // loop through all the adjacent nodes of currentNodeIndex
        // if a adjacent has not been visited, then mark it visited
        // and push it
        for (int i = 0; i < graph->numberOfNodes; ++i) {
            if (graph->adjacencyMatrix[currentNodeIndex][i] != INF && !visited[i]) {
                visited[i] = true;
                stack_push(stack, i);
                distances_list[++visited_count] = i;
            }
        }
    }
    return distances_list;
}