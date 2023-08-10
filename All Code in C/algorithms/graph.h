#define INF 9999
#define MAX_NODES 100

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

/**
 * A node is represented by the following :
 * 1. The node number.
 * 2. The distance from the source node.
*/
struct Node {
    char *name;
    int index;
//    int distance;
} typedef Node;

/**
 * A graph is represented by the following :
 * 1. The adjacency matrix is a 2D array of integers.
 * 2. The number of nodes in the graph.
 * 3. The number of edges in the graph.
*/
struct Graph {
    int numberOfNodes;
    int adjacencyMatrix[MAX_NODES][MAX_NODES];
    Node *nodes[MAX_NODES];
} typedef Graph;

/**
 * This struct is used to store the distance of each node from 
 * the source node.
*/
struct distArray {
    int nodeIndex;
    int distance;
} typedef distArray;

/**
 * initializes a graph to have no nodes or edges.
 * and all edges to have a weight of infinity.
 * 
 * Example : adjacencyMatrix[i][j] = distance from node i to node j.
 *  
 * @param graph the graph to initialize.
*/
Graph* initializeGraph() {
    Graph *graph = (Graph *) malloc(sizeof(Graph));
    graph->numberOfNodes = 0;

    // initialize all the edges to INF and nodes to NULL.
    for (int i = 0; i < MAX_NODES; i++) {
        graph->nodes[i] = NULL;
        for (int j = 0; j < MAX_NODES; j++) {
            graph->adjacencyMatrix[i][j] = INF;
        }
    }

    return graph;
}

/**
 * adds a node to the graph with the given name.
 * creates a node, and adds it to graph.
 * 
 * @param 
*/
int add_to_graph(Graph* graph, char *nodeName) {
    // 1. get the index
    int index = graph->numberOfNodes;

    // 2. create the node
    Node* node = (Node*) malloc(sizeof(Node));
    node->name = (char*) malloc(strlen(nodeName) + 1);
    strcpy(node->name, nodeName);
    node->index = index;

    // 3. add node to the graph
    graph->nodes[index] = node;
    graph->numberOfNodes++;

    return index;
}

/**
 * Sets the edge index based on the source and destination.
 * For example : set_edge_distance(&graph, "paris", "lille", 50)
 * 
 * 
*/
int set_edge_distance(Graph *graph, 
                      char *src, char *dest, int weight) {
    
    int src_index = -1; int dest_index = -1;
    
    // find the index of the source node.
    for (int i = 0; i < graph->numberOfNodes; i++) {
        char *current_name = graph->nodes[i]->name;
        if (strcmp(current_name, src) == 0 ) {
            src_index = i; }
        else if (strcmp(current_name, dest) == 0 ) {
            dest_index = i; }
        else if (src_index != -1 && dest_index != -1) {
            break; }
    }

    // if node not found return
    if (src_index == -1 || dest_index == -1) {
        return -1;
    }

    // if node found edit the distance
    graph->adjacencyMatrix [src_index] [dest_index] = weight;
    return 1;
}

/**
 * Frees the graph.
 * 
 * @param graph the graph to free.
*/
void free_graph(Graph *graph) {
    for (int i = 0; i < graph->numberOfNodes; i++) {
        free(graph->nodes[i]->name);
        free(graph->nodes[i]);
    }
    free(graph);
}

/**
 * Prints the graph.
 * In the format :
 * 1. node1 -> node2 (distance)
 * 
 * @param graph the graph to print.
*/
void print_graph(Graph *graph) {
    if (graph == NULL) {
        printf("Graph is empty.\n");
        return;
    }

    printf("\n\nNumber of nodes : %i\n", graph->numberOfNodes);
    printf("----------------------------------------\n");

    for (int i = 0; i < graph->numberOfNodes; i++) {
        for (int j = 0; j < graph->numberOfNodes; j++) {
            if (graph->adjacencyMatrix[i][j] == INF) {
                continue;
            }
            else {
                printf("%s -> %s (%i)\n",
                       graph->nodes[i]->name,
                       graph->nodes[j]->name,
                       graph->adjacencyMatrix[i][j]);
            }
        }
    }
    printf("----------------------------------------\n");
}

/**
 * Uses an array, iterates over the graph and prints the distances.
 *
 * @param graph the graph to print.
 * @param name the name of the source node.
 * @return the index of the source node.
 */
int get_index(Graph *graph, char *name) {
    for (int i = 0; i < graph->numberOfNodes; i++) {
        if (strcmp(graph->nodes[i]->name, name) == 0) {
            return i;
        }
    }
    return -1;
}

/**
 * This function reads a file and returns a string containing the contents of the file.
 *
 * @param filename the name of the file to read.
 * @return  a string containing the contents of the file.
 */
char *read_file(const char *filename) {
    FILE *f = fopen(filename, "rb");
    if (f == NULL) {
        perror("Error opening file");
        return NULL;
    }

    fseek(f, 0, SEEK_END);
    long fsize = ftell(f);
    fseek(f, 0, SEEK_SET);

    char *string = malloc(fsize + 1);
    fread(string, fsize, 1, f);
    fclose(f);

    string[fsize] = '\0';
    return string;
}

/**
 * Intializes a graph and adds vertices and distances from a string.
 *
 * @param vertices List of vertices in the format: <vertex1>\n<vertex2>\n...
 * @param distances List of distances in the format: <source> <destination> <weight>\n...
 * @return a graph containing the vertices and distances from the string.
 */
Graph* graph_from_string(char* vertices, char* distances) {

    // initialize graph
    Graph *graph = initializeGraph();

    char *vertices_copy = strdup(vertices);
    char *distances_copy = strdup(distances);

    // read each line and create vertices
    char *line = strtok(vertices_copy, "\n");
    while (line != NULL) {
        // create a new node
        int index = add_to_graph(graph, line);
        line = strtok(NULL, "\n");
    }

    // read each line and create edges
    char *line2 = strtok(distances_copy, "\n");
    while (line2 != NULL) {
        char source[100], destination[100]; int weight;
        sscanf(line2, "%s %s %d", source, destination, &weight);
        set_edge_distance(graph, source, destination, weight);
        line2 = strtok(NULL, "\n");
    }

    free(vertices_copy); free(distances_copy);

    return graph;
}

/**
 * Intializes a graph and adds vertices and distances from a file.
 *
 * @param vertices_file Path to file containing vertices in the format: <vertex1>\n<vertex2>\n...
 * @param distances_file Path to file containing distances in the format: <source> <destination> <weight>\n...
 * @return a graph containing the vertices and distances from the file.
 */
Graph* graph_from_file(const char *vertices_file, const char *distances_file) {
    char* stringVertices = read_file(vertices_file);
    char *stringDistances = read_file(distances_file);

    if (stringVertices == NULL) {
        perror("Error opening file for distances.");
        return NULL;
    } else if (stringDistances == NULL) {
        perror("Error opening file for distances.");
        return NULL;
    }

    return graph_from_string(stringVertices, stringDistances);
}
