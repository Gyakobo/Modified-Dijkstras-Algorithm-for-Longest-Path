import heapq

def longest_path(graph, start):
    # Initialize distances
    distances = {node: float('-inf') for node in graph}
    distances[start] = 0

    # Max-heap priority queue
    max_heap = [(-0, start)]
    heapq.heapify(max_heap)





