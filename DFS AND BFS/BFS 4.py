graph = {
    0: [1],
    1: [3],
    2: [1],
    3: [2, 4],
    4: [5],
    5: [6],
    6: [4],
    7: [6]
}

visited = set()
queue = [0]

while queue:
    node = queue.pop(0)
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        queue.extend(i for i in graph[node] if i not in visited)
