import heapq

def longest_path(graph, start):
    # Initialize distances
    distances = {node: float('-inf') for node in graph}
    distances[start] = 0

    # Max-heap priority queue
    max_heap = [(-0, start)]
    heapq.heapify(max_heap)

    while max_heap:
        current_distance, current_node = heapq.heappop(max_heap)
        current_distance = -current_distance

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance > distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(max_heap, (-distance, neighbor))

    return distances