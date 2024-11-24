def astar(graph, cost, source, destination):
    open, closed = {source}, []  
    g = {source: 0}
    while open:
        current = min(open, key=lambda x: (g[x] + cost[x], g[x]))
        print('Open list: ', open, '\nClosed list: ', closed, '\n')
        open.remove(current)
        closed.append(current)
        #print(f"Open list: {open}")
        #print(f"Closed list: {closed}")
        if current == destination:
            path_cost = g[current]
            print(f"Total path cost: {path_cost}")
            return closed
        for v, w in graph[current].items():
            temp = g[current] + w
            if v not in g or temp < g[v]:
                g[v] = temp
                open.add(v)
    return closed
graph = {
    'A': {'D': 4, 'C': 5, 'B': 9},
    'B': {'E': 8, 'A': 1},
    'C': {'E': 6, 'F': 8, 'A': 5},
    'D': {'F': 4, 'A': 8},
    'E': {'H': 9, 'C': 1, 'B': 4},
    'F': {'C': 1, 'G': 5},
    'G': {'H': 3, 'F': 8},
    'H': {'E': 1, 'G': 4}
}
cost = {'A': 40, 'B':32, 'C':25, 'D':35, 'E':19, 'F':17, 'G':20, 'H':0}
path = astar(graph, cost, 'A', 'H')
print("Closed list (path to goal):", path)
