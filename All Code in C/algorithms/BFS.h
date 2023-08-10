#include "graph.h"
#include "myQueue.h"

/*
 * Psuedo code for BFS:
 * 1. Create a queue
 * 2. Enqueue the source node
 * 3. *** visit all unvisited adjacent nodes of the current node ***
 * 4. *** mark the adjacent nodes as visited and enqueue them ***
 * 5. current node = dequeued node
 * 6. repeat 3, 4, 5 until queue is empty
 *
 * @param graph the graph to traverse.
 * @param sourceNodeIndex the index of the source node.
 *
 * */
void bfs(Graph *graph, int sourceNodeIndex) {
    // create a queue for BFS
    bool visited[MAX_NODES] = {false};
    struct Queue *queue = createQueue();
    int* distances_list = (int*) malloc(sizeof(int) * graph->numberOfNodes);
    int visited_count = 0; // to keep track of the number of visited nodes

    // set the start node to visited
    visited[sourceNodeIndex] = true;
    enqueue(queue, sourceNodeIndex);
    distances_list[visited_count++] = sourceNodeIndex; // Add source node to the list

    // loop until queue is empty
    while (!isEmpty(queue)) {
        // get the next node from the queue
        int currentNodeIndex = dequeue(queue);
        printf("%s ", graph->nodes[currentNodeIndex]->name);

        // loop through all the adjacent nodes of currentNodeIndex
        // if a adjacent has not been visited, then mark it visited
        // and enqueue it
        for (int i = 0; i < graph->numberOfNodes; ++i) {
            if (graph->adjacencyMatrix[currentNodeIndex][i] != INF && !visited[i]) {
                visited[i] = true;
                enqueue(queue, i);
                distances_list[visited_count++] = i;
            }
        }
    }
}