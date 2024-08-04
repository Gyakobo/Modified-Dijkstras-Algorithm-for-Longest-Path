# Modified Dijkstra's Algorithm for Longest Path

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white)

Author: [Andrew Gyakobo](https://github.com/Gyakobo)

## Introduction

To adapt Dijkstra's algorithm to find the longest path instead of the shortest, we need to make a few key modifications. Dijkstra's algorithm is designed to find the shortest path in a graph by always expanding the shortest known distance. To find the longest path, we need to adjust this logic.

## Methodology

### Modified Dijkstra's Algorithm for Longest Path

1. Initialize Distances:

    * Instead of initializing distances to infinity, initialize them to negative infinity. This is because we are looking for the maximum distance.
    
    * Set the distance to the starting node (PVD) to 0.

2. Priority Queue:

    * Use a priority queue to store nodes to be explored, but prioritize nodes with the longest known distance. You can use a max-heap for this purpose.

3. Relaxation:

    * During the relaxation step, instead of updating the shortest distance, update the longest distance. For each adjacent node, if the known distance to the adjacent node can be increased by traveling through the current node, update the distance and add the node to the priority queue.

4. Stop Condition:

    * Unlike the shortest path, the longest path in a graph with cycles can be infinite. Ensure the graph is a Directed Acyclic Graph (DAG) to avoid this. For practical scenarios like finding a route on a flight map, the graph is typically a DAG because flights don't loop infinitely.

### Steps of the Modified Algorithm

1. Initialize

    * Set the distance to the source node (PVD) to 0 and all other nodes to negative infinity.

    * Initialize the priority queue with the source node.

2. Process the Priority Queue:

    * Extract the node with the maximum distance from the priority queue.

    * For each neighbor of the extracted node, check if the distance to the neighbor can be increased by going through the extracted node.

    * If yes, update the distance and add the neighbor to the priority queue.

3. Continue until queue is empty:

    * Continue the process until the priority queue is empty.

## License
MIT