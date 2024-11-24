def gbfs(graph, cost, source, destination):
    open = []
    closed = []
    open.append(source)
    print('Open list: ', open, '\nClosed list: ', closed, '\n')
    if not graph[source]:
        return []
    while destination not in closed:
        open.remove(source)
        closed.append(source)
        for i in graph[source]:
            if i not in closed:
                open.append(i)
        source = min(open, key= lambda x: cost[x])
        print('Open list: ', open, '\nClosed list: ', closed, '\n')
    return closed
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'E', 'F'],
    'D': ['A', 'F'], 
    'E': ['B', 'C', 'H'],
    'F': ['C', 'G'],
    'G': ['F', 'H'],
    'H': ['E', 'G']
}
cost = {'A': 40, 'B':32, 'C':25, 'D':35, 'E':19, 'F':17, 'G':0, 'H':10}
final = gbfs(graph, cost, 'A', 'G')
total_cost=0
for node in final:
    total_cost += cost[node]
print(f'Total cost: {total_cost}')
print('Path :', ' -> '.join(final))