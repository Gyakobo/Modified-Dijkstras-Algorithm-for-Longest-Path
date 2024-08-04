import heapq

graph = {
    'PVD': [('A', 500), ('C', 600), ('E', 300)],
    'A': [('B', 1000)],
    'B': [('HNL', 2500)],
    'C': [('D', 900)],
    'D': [('HNL', 2600)],
    'E': [('F', 700)],
    'F': [('HNL', 2400)],
    'HNL': []
}

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

# Run the modified Dijkstra's algorithm
distances = longest_path(graph, 'PVD') 

print(distances)
# print(f'Longest Path: {di}')