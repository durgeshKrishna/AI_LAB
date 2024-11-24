import heapq

def ucs(graph, start, stop):
    # Priority queue, stores tuples of (cost, node, path)
    # queue = [(0, start, [start])]
    queue=[]
    heapq.heappush(queue,(0,start,[start]))
    visited = set()

    while queue:
        # Pop the node with the lowest cost
        cost, node, path = heapq.heappop(queue)

        if node == stop:
            print(f"Path found: {' -> '.join(path)} with total cost: {cost}")
            return True

        if node not in visited:
            visited.add(node)
            
            for neighbor, path_cost in graph[node]:
                if neighbor not in visited:
                    # Push the neighbor with updated cost and path
                    heapq.heappush(queue, (cost + path_cost, neighbor, path + [neighbor]))
                    
    print(f"No path found from {start} to {stop}")
    return False

# Graph structure with nodes and edge costs
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 4), ('D', 7)],
    'C': [('A', 5), ('B', 4), ('D', 2), ('E', 3)],
    'D': [('B', 7), ('C', 2), ('E', 1)],
    'E': [('C', 3), ('D', 1)]
}

start = 'A'
stop = 'E'

# Call UCS to find the least-cost path and total cost
ucs(graph, start, stop)
