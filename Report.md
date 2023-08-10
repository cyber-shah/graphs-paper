<!-- TOC -->

- [Final Report - Path Finders and A\* Algorithm](#final-report---path-finders-and-a-algorithm)
- [0 - Abstract](#0---abstract)
- [1 - Introduction](#1---introduction)
    - [ 1.1 - Why Path Finding? ](#-11---why-path-finding-)
    - [ 1.2 - What is Path Finding? ](#-12---what-is-path-finding-)
    - [ 1.3 - How do computers find paths? ](#-13---how-do-computers-find-paths-)
    - [ 1.4 Algorithms covered ](#-14-algorithms-covered-)
- [2 - Background and Theory](#2---background-and-theory)
  - [Question 1: Is there a path between node A and node B?](#question-1-is-there-a-path-between-node-a-and-node-b)
    - [1.1 - Depth First Search](#11---depth-first-search)
  - [Question 2 : What is the shortest path between A to B?](#question-2--what-is-the-shortest-path-between-a-to-b)
    - [2.1 - Breadth First Search](#21---breadth-first-search)
    - [2.2 - Dijkstra's Algorithm](#22---dijkstras-algorithm)
    - [2.3 - A\* Algorithm](#23---a-algorithm)
- [3 - Implementation Details](#3---implementation-details)
- [4 - Testing and Validation](#4---testing-and-validation)
- [5 - Results and Discussion](#5---results-and-discussion)
- [6 - Conclusion](#6---conclusion)
- [7 - Future Work](#7---future-work)
- [8 - References](#8---references)

<!-- /TOC -->

# Final Report - Path Finders and A* Algorithm
* **Author**: Pranchal Shah
* **GitHub Repo**: [5008 Repo](www.github.com/cyber-shah/5008-Project)
* **Semester**: Summer 2023
* **Languages Used**: C and Python

# 0 - Abstract

The purpose of this report is to discuss the implementation of various path finding algorithms and their performance. The algorithms discussed in this report are Depth First Search, Breadth First Search, Dijkstra's Algorithm and A* Algorithm. The report will discuss the theory behind each algorithm, their implementation details, testing and validation, results and discussion, conclusion and future work. The report will also discuss the performance of each algorithm and compare them with each other.

The report will also discuss the pros and cons of each algorithm and their use cases. The report will also discuss the performance of each algorithm in different scenarios and compare them with each other. The goal is to understand the implementation details of each algorithm and their performance in different scenarios.

The algorithms are tested on the following criteria:
1. Shortest path
2. Nodes explored to find the shortest path
3. Time taken to find the shortest path
4. Memory used to find the shortest path
5. Performance on different graphs
6. Performance on different grid sizes
7. Performance on different obstacles
8. Performance on different edge weights
9. Variying start and end nodes

The algorithms are tested on the following conditions:
1. A simple graph weighted edges
2. A grid of nodes each with uniform edge weight and no obstacles and a pretty straight forward shortest path
3. A maze with obstacles and many shorter paths



# 1 - Introduction

### <u> 1.1 - Why Path Finding? </u>
Path finding has been a very important problem in computer science. It has been used in many applications such as logistics planning, least cost call or IP routing, and gaming simulation. 
I got really intrested into it when I learned that a logistics company (UPS) collceted years of data and used algorithms to navigate better.
UPS says it’s saved 10 million gallons of fuel, avoided the emission of 20,000 tons of CO2, and delivered 350,000 more packages a year, just due to efficient path finding!
More on that here: [Science Behind UPS Trucks!](https://bigthink.com/technology-innovation/the-science-behind-why-ups-trucks-avoid-making-left-turns/)

I was also intrested in it because I am a largely intrested in video games and I wanted to learn how video games work. I also wanted to learn how self driving cars work. I learned that path finding is a very important part of both of these applications and it solves a very important problem. A problem that we as humans encounter almost everyday.


<img src = https://happycoding.io/tutorials/libgdx/images/pathfinding-12.png> 

Image Source: [Happy Coding/ Path finding](https://happycoding.io/tutorials/libgdx/pathfinding)

### <u> 1.2 - What is Path Finding? </u>
Path finding is the process of finding a path between two points in a graph.
A graph is a data structure that consists of nodes and edges. The nodes are the points in the graph and the edges are the connections between the nodes. The edges can be weighted or unweighted. The weight of an edge is the cost of traversing that edge. The cost can be anything such as distance, time, fuel, etc. The edges can also be directed or undirected. The directed edges are one way and the undirected edges are two way.

The goal of path finding is to find the shortest path between two nodes in a graph. The path can be defined as the sequence of nodes that need to be traversed to reach the destination node from the source node.  

### <u> 1.3 - How do computers find paths? </u>
A computer starts at a souce node and then starts 'scanning' or 'exploring' the graph. It scans the graph by exploring the nodes and edges. It explores the nodes and edges by traversing them. The computer traverses the nodes and edges by following the edges. The computer follows the edges by selecting the edge with the lowest cost. 

An analogy to it would be like a blind person trying to find the shortest path between two points. Instead of using his eyes to see the path, he uses his hands to feel the path. He follows on one path and then feels the edges to see if there is a better path. If there is a better path, he follows that path. He keeps doing this until he reaches the destination.

### <u> 1.4 Algorithms covered </u>
The algorithms covered in this report are:
1. Depth First Search
2. Breadth First Search
3. Dijkstra's Algorithm
4. A* Algorithm







# 2 - Background and Theory
Graph traversal algorithms form the backbone of various computational processes, from deciphering networks to enabling efficient pathfinding. These algorithms are instrumental in navigating the intricate web of connections that graphs represent. One fundamental class of graph traversal algorithms includes Depth First Search (DFS), which excels in exploring the depths of a graph's structure.

In this section, we will delve into the theoretical foundations of DFS, its operational principles, and its applicability across various scenarios. By understanding DFS in the context of graph traversal algorithms, we can appreciate its unique strengths and limitations as we delve deeper into its mechanics.

Each algorithm is divided into the following sections:
1. History
2. Overiew of how it works
3. Advanatages
4. Disadvantages
5. Complexity
6. Use cases
7. Psuedo code

The algorithms can be divided into two parts here: 1 that help us find out IF a path exists and 2 that help us find the SHORTEST path. The algorithms that help us find out IF a path exists are: DFS and BFS. The algorithms that help us find the SHORTEST path are: Dijkstra's Algorithm and A* Algorithm.

## Question 1: Is there a path between node A and node B?
The two algorithms that help us find out IF a path exists are: DFS and BFS. 
> All the GIFs shown in this section are made by me, unless  otherwise stated. 
>  Kindly note that the algorithms have been implemented by me and pygame is used to create animations. The pygame animation code can be found here : [pyGame_Vizs.py](vizs/pyGame_Vizs.py)

### 1.1 - Depth First Search
   1. **_History_**: 
      - Depth First search dates back to 19th century. It was first used by French mathematician Charles Pierre Trémaux as a strategy for solving mazes. 
      - DFS is was pretty much the background for most of the modern day path finding algorithms. From Bellman Ford to Dijkstra to A* to Prim's Algorithm, have all built on top of DFS.
      - It's simplicity and efficiency makes it a very popular algorithm. It is also very easy to implement.
   2.  **Overview of how it works_**:  
       - Depth First Search is a graph traversal algorithm that starts at a source node and explores the graph by traversing the edges. 
       - It follows a single path until it reaches a dead end. It then backtracks to the previous node and explores the next path. It keeps doing this until it reaches the destination node. 
       - It then backtracks from the destination node to the source node to find the shortest path. It uses a stack to keep track of the nodes that need to be explored. It uses a parent array to keep track of the path. The parent array is used to backtrack from the destination node to the source node. The parent array is also used to find the number of nodes explored to find the shortest path.
       - ![DFS-basic](graphics/basic-DFS.gif)
   3.  **_Advantages_**: 
       - The advantage of DFS is that it is very simple to implement. 
       - It is also very fast and uses very little memory. 
       - It can quickly determine if a graph has cycles.
   4. **_Disadvantages_**: 
      - It does not guarantee the shortest path. 
      - It can get stuck in a loop. 
      - The other disadvantage is that it may keep moving down the wrong path and may be too late to backtrack towards the right path.
   5. **_Complexity_**:
      | Approach | Time Complexity | Space Complexity |
      | --- |----------------| --- |
      | Adjacency Matrix | $O(V^2)$        | $O(V)$ |
      | Adjacency List | $O(V + E)$           | $O(V + E)$ |
      The implementation in this report uses an adjacency matrix, just because it is easier to implement.
   6. **_Use Cases_**:
      - DFS is used in maze generation algorithms.
      - It is also used in topological sorting.
      - DFS is used in finding connected components in a graph.
      - It is also used in cycle detection in a graph.
   7. **_Psuedocode_**:
      ```
      DFS(Graph,vertex v)
         Stack S
         for each vertex u, set visited[u] := false;
         push S, v;
         while (S is not empty) do
            u := pop S;
            if (not visited[u]) then
               visited[u] := true;
               for each unvisited neighbour w of u
                  push S, w;
      ```


## Question 2 : What is the shortest path between A to B?
So by now we know how to solve the question of `is there a path between A to B?`. Now the next two algorithms will help us solve the question of `what is the shortest path between A to B?`.
### 2.1 - Breadth First Search

1. **_History_**:  
      - Breadth First Search was invented by Konrad Zuse in 1945. 
      - It was later rediscovered by Edsger Dijkstra in 1959. 
      - It is also known as the `Breadth First Traversal` or `Breadth First Walk`.
      - It is a graph traversal algorithm that starts at a source node and explores the graph by traversing the edges.
      - BFS is a core algorithm in computer science and is widely used in fields like network routing, social network analysis, and more.

2.  **_Overview of how it works_**: 
       - It operates in a similar way to DFS, but it uses a queue instead of a stack. 
       - It starts from the source node and explores it neighbours in `layers`. Layers are nothing but the nodes that are at a distance of `n` from the source node. So the first layer contains nodes that are at a distance of 1 from the source node. The second layer contains nodes that are at a distance of 2 from the source node and so on.
       - It explores the first layer first, then the second layer and so on. This means that nodes closer are explored first and nodes farther away are explored later.
   ![BFS-basic](graphics/basic-BFS.gif)
   
3. **_Advantages_**: 
      - BFS is guaranteed to find the shortest path between the source node and the destination node.
      - If the graph is connected, then BFS can be used to find the shortest path between all the nodes in the graph.
      - It explores the graph in layers which can be useful if we need to analyse the neighbours.
      - It does not visit a node more than once.

4. **_Disadvantages_**: 
      - It is less suitable for weighted graphs. In a weighted graph, where edges have different costs or distances, the standard BFS will not necessarily find the shortest path. This is because BFS explores nodes in layers, and the order in which nodes are explored might not correspond to the shortest path.
      - It uses more memory than DFS.

5. **_Complexity_**:
      | Approach | Time Complexity | Space Complexity |
      | --- |----------------| --- |
      | Adjacency Matrix | $O(V^2)$        | $O(V)$ |
      | Adjacency List | $O(V + E)$           | $O(V + E)$ |
      The implementation in this report uses an adjacency matrix, just because it is easier to implement.
6. **_Use Cases_**:
   - BFS is used in shortest path algorithms, especially when the graph is unweighted or equally weighted.
   - It is employed for finding the shortest path between nodes in a graph.
   - BFS can be used to explore hierarchical structures or levels of depth in graphs.
   - It's useful for determining connected components in a graph.
7. **_Psuedocode_**:
      ```
      BFS(Graph, start_vertex)
         Queue Q
         visited = set()
         enqueue Q, start_vertex
         visited.add(start_vertex)
         while Q is not empty do
            vertex = dequeue Q
            for each neighbor w of vertex do
               if w is not in visited then
                  visited.add(w)
                  enqueue Q, w
      ```

### 2.2 - Dijkstra's Algorithm

1. **_History_**:  
      - Dijkstra's Algorithm was invented by Edsger Dijkstra in 1956. The technique first appeared as a solution to the problem of finding the shortest path between nodes in a weighted graph.
      - It has been widely used in real-world applications, including routing in computer networks and navigation systems.
      - It is also known as the `Shortest Path First Algorithm`.
      - It was invented to solve the problem of finding the shortest path between nodes in a weighted graph.
2. **_Overview of how it works_**:
      - Dijkstra's Algorithm is a graph traversal algorithm that starts at a source node and explores the graph by traversing the edges. It is mainly used to find shortest path between nodes in a weighted graph. 
      - It is similar to BFS, but uses a concept called `edge relaxation`. Which means that it relaxes the edges of the graph by updating the distance of the nodes.
      - While visiting nodes it maintains a distance array which stores the distance of each node from the source node. Initially the distance of all the nodes is set to infinity. And the distance of the source node is set to 0. 
      - These distances are updated as the algorithm progresses.
      - The process ends when all the nodes have been visited and returns a list of shortest distances from the source node to all the other nodes. 
      
      <img src = https://upload.wikimedia.org/wikipedia/commons/e/e4/DijkstraDemo.gif>
      
      Image source : [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:DijkstraDemo.gif") 
3. **_Advantages_**: 
   - Dijkstra's Algorithm is guaranteed to find the shortest path between the source node and the destination node.
   - The basic concept is straightforward to understand and implement.
   - It is also very efficient.
4. **_Disadvantages_**:
   - It does not work with negative edge weights.
   - Limited to Positive Weights: It doesn't work well with negative edge weights as negative cycles can cause the algorithm to fail.
   - Might not be most suitable for large graphs.
5. **_Complexity_**:
         | Approach | Time Complexity | Space Complexity |
      | --- |----------------| --- |
      | Adjacency Matrix | $O(V^2)$        | $O(V)$ |
      | Adjacency List | $O(V + E)$           | $O(V + E)$ |

      

### 2.3 - A* Algorithm
1.  **_Concept_**:
   - The concept of A* is similar to Dijkstra's Algorithm, but it uses a concept called `heuristics`.
   - Heuristics is a way to estimate the distance between two nodes. It is used to estimate the distance between the current node and the destination node. 
   - Rather than checking every single route, like Djikstra or BFS, heuristic algorithms only check the most promising routes. They take an educated guess on which route is the best route.
  2. **_Advantages_**: 
      - The advantage of A* is that it is very fast and efficient. 
      - It is also very simple to implement. 
      - It is also very easy to understand.


| Approach | Time Complexity | Space Complexity |
| --- |----------------| --- |
| Depth First Search | $O(n)$          | $O(1)$ |
| Breadth First Search | $O(2^n)$        | $O(n)$ |
| Djikstra | $O(n)$           | $O(n)$ |
| A* | $O(n)$           | $O(n)$ |

# 3 - Implementation Details
<!-- ![20x20Djikstra](viz/Djikstra-20x20.gif) -->

# 4 - Testing and Validation

# 5 - Results and Discussion

<!-- ![20x20DFS](viz/DFS-20x20.gif) -->
# 6 - Conclusion

# 7 - Future Work

# 8 - References



