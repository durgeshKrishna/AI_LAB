def dls(graph, node, stop, limit, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [node]
    if node == stop:
        print(f"Path found: {' -> '.join(path)}")
        return True
    if limit <= 0:
        return False
    visited.add(node)
    for neighbor, _ in graph[node]:
        if neighbor not in visited:
            if dls(graph, neighbor, stop, limit - 1, path + [neighbor], visited):
                return True
    return False
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 4), ('D', 7)],
    'C': [('A', 5), ('B', 4), ('D', 2), ('E', 3)],
    'D': [('B', 7), ('C', 2), ('E', 1)],
    'E': [('C', 3), ('D', 1)]
}
start = 'A'
stop = 'E'
limit = 3  
if not dls(graph, start, stop, limit):
    print(f"No path found from {start} to {stop} within depth limit {limit}")
