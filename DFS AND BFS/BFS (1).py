graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [5],
    5: []
}

visited = set()
queue = [1]

while queue:
    node = queue.pop(0)
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        queue.extend(i for i in graph[node] if i not in visited)
