//
// Created by shahp on 8/8/2023.
//

#ifndef FINAL_RESEARCH_ASTAR_PATHFINDER_MYQUEUE_H
#define FINAL_RESEARCH_ASTAR_PATHFINDER_MYQUEUE_H

#endif //FINAL_RESEARCH_ASTAR_PATHFINDER_MYQUEUE_H


#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define MAX_NODES 100 // Maximum number of nodes in the graph

// Queue implementation for BFS
struct Queue {
    int items[MAX_NODES];
    int front, rear;
};

struct Queue* createQueue() {
    struct Queue* queue = (struct Queue*)malloc(sizeof(struct Queue));
    queue->front = -1;
    queue->rear = -1;
    return queue;
}

bool isEmpty(struct Queue* queue) {
    return queue->front == -1;
}

void enqueue(struct Queue* queue, int item) {
    if (isEmpty(queue)) {
        queue->front = 0;
    }
    queue->rear++;
    queue->items[queue->rear] = item;
}

int dequeue(struct Queue* queue) {
    int item = queue->items[queue->front];
    queue->front++;
    if (queue->front > queue->rear) {
        queue->front = queue->rear = -1;
    }
    return item;
}