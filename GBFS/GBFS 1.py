graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['E', 'F'],
    'D': ['F'],
    'E': ['H'],
    'F': ['G'],
    'G': ['H'],
    'H': []
}

h = {
    'A': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'G': 0,
    'H': 10
}

def greedy_bfs(start, goal):
    open_list = [start]
    visited = set()

    while open_list:
        open_list.sort(key=lambda node: h[node])
        node = open_list.pop(0)

        if node in visited:
            continue

        print(node, end=" ")
        visited.add(node)

        if node == goal:
            print("\nGoal reached!")
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                open_list.append(neighbor)

    print("\nGoal not found!")

greedy_bfs('A', 'G')
