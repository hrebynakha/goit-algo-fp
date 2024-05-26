"""
Завдання 3. Дерева, алгоритм Дейкстри

Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі,
використовуючи бінарну купу.
Завдання включає створення графа,
використання піраміди для оптимізації вибору вершин та обчислення найкоротших шляхів
від початкової вершини до всіх інших.
"""

import heapq
import networkx as nx

def dijkstra(graph, start):
    ## add infinity distance to all out pathes
    shortest_paths = {node: float('inf') for node in graph.nodes}
    shortest_paths[start] = 0
    # init value, 0 for start
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbor, attrs in graph[current_node].items():
            weight = attrs['weight']
            distance = current_distance + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return shortest_paths

# add graph
G = nx.Graph()
G.add_edge('A', 'B', weight=1)
G.add_edge('A', 'C', weight=4)
G.add_edge('B', 'C', weight=2)
G.add_edge('B', 'D', weight=5)
G.add_edge('C', 'D', weight=1)
start = 'A'
shortest_paths = dijkstra(G, start)
print(f"Shortest paths from {start}:")
for ver, distance in shortest_paths.items():
    print(f"Distance to {ver}: {distance}")
