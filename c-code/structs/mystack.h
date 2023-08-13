/*  ========== H03 - Personal Stack Implementation ============
 *
 *   Student: Pranchal Shah
 *   Semester: Summer 2023
 *
 * A simple stack implementation to hold int values.
 *
 */

#ifndef MYSTACK_H
#define MYSTACK_H
#include <stdio.h>  // For IO operations
#include <stdlib.h> // for malloc/free

/** Stores the maximum 'depth' of our stack.
(i.e. capacity cannot exceed MAX_DEPTH for any stack) **/
#define MAX_DEPTH 32

/** Create a node data structure to store data within
our stack. In our case, we will stores 'integers' */
typedef struct node
{
    int data;
    struct node *next;
} node_t;

/** Create a stack data structure
* Our stack holds a single pointer to a node, which
* is a linked list of nodes. 
**/
typedef struct stack
{
    int count;             // count keeps track of how many items
                           // are in the stack.
    unsigned int capacity; // Stores the maximum size of our stack
    node_t *head;          // head points to a node on the top of our stack.
} neu_stack;

/**  Creates a stack
* Returns a pointer to a newly created stack.
* The stack should be initialized with data on the heap.
* (Think about what the means in terms of memory allocation)
* The stacks fields should also be initialized to default values.
*/
neu_stack* create_stack(unsigned int capacity)
{
    // create a pointer to neu_stack called myStack
    neu_stack* myStack = (neu_stack*) malloc (sizeof(neu_stack));
    // initialize the fields of myStack
    if (capacity > MAX_DEPTH) {
        myStack->capacity = MAX_DEPTH;
    }
    else if (capacity == 0) {
        myStack->capacity = MAX_DEPTH;
    }
    else {
        myStack->capacity = capacity;
    }
    myStack->count = 0;
    myStack->head = NULL;

    // return the pointer to neu_stack
    return myStack;
}

/** Check if the stack is empty
* Returns 1 if true (The stack is completely empty)
* Returns 0 if false (the stack has at least one element enqueued)
*/
int stack_empty(neu_stack* stack)
{
    if (stack->count == 0) {
        return 1;
    }
    else {
        return 0;
    }
}

/** Check if the stack is full
* Returns 1 if true (The Stack is completely full, i.e. equal to capacity)
* Returns 0 if false (the Stack has more space available to enqueue items)
**/
int stack_full(neu_stack* stack)
{
    if (stack->count == stack->capacity) {
        return 1;
    }
    else {
        return 0;
    }
}

/** Enqueue a new item
* i.e. push a new item into our data structure
* Returns a -1 if the operation fails (otherwise returns 0 on success).
*    -> if the Stack is full that is an error, but does not crash the program.
**/
int stack_push(neu_stack *stack, int item)
{
    // check if no item can be added
    if (stack_full(stack) == 1) {
        return -1;
    }
    else {
        // 1. create a new node
        node_t* new_node = (node_t*) malloc(sizeof(node_t));
        // 2. set the data
        new_node->data = item;
        // 3. set head
        new_node->next = stack->head;
        // 4. change head
        stack->head = new_node;
        // 5. add 1 to count
        stack->count++;
        return 0;
    }
}

/** Dequeue an item
*   Returns the item at the front of the stack and
*   removes an item from the stack.
*   Removing an item from the empty stack should
*   print to stderr, and return the EXIT_FAILURE value
*   Example:
     fputs("no items to dequeue!\n", stderr);
     return EXIT_FAILURE
**/
int stack_pop(neu_stack* stack)
{
    // check if no item can be removed
    if (stack->head == NULL) {
        fputs("no items to dequeue!\n", stderr);
        return EXIT_FAILURE;
    }
    else {
        int item = stack->head->data;
        node_t* temp = stack->head;
        stack->head = stack->head->next;
        free(temp);
        // 5. subtract 1 from count
        stack->count--;
        return item;
    }
}


/** returns the size of the stack. If the
 * stack hasn't been properly recreated, print to stderr, 
 * and return -1 
*/
unsigned int stack_size(neu_stack* stack)
{
    // check if the stack hasn't been created
    if (stack == NULL) {
        fputs("stack hasn't been properly recreated!\n", stderr);
        return -1;
    }
    // else return count
    else {
        return stack->count;
    }
}


/** Removes a stack and ALL of its elements from memory.
 *  This should be called before any program terminates.
 *  Simple ignores if an invalid stack is passed to it.
 **/
void free_stack(neu_stack* stack)
{
    node_t* temp = stack->head;

    while (temp != NULL) {
        temp = stack->head->next;
        free(stack->head);
        stack->head = temp;
    }

    free(stack);

}

#endif