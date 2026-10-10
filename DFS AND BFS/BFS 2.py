graph = {
    1: [2, 7],
    2: [3, 6],
    3: [4, 5],
    4: [],
    5: [],
    6: [],
    7: [8, 10],
    8: [9],
    9: [],
    10: []
}

visited = set()
queue = [1]

while queue:
    node = queue.pop(0)
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        queue.extend(i for i in graph[node] if i not in visited)
