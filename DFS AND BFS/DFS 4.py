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

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for i in graph[node]:
            dfs(i)

dfs(0)
