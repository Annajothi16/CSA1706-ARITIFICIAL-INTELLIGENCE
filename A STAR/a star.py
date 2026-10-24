graph = {
    'S': {'A': 3, 'D': 4},
    'A': {'B': 4, 'D': 5},
    'B': {'C': 4, 'E': 5},
    'D': {'E': 2},
    'E': {'F': 4},
    'F': {'G': 3.5},
    'C': {},
    'G': {}
}

h = {
    'S': 0,
    'A': 10.1,
    'B': 5.8,
    'C': 3.4,
    'D': 9.2,
    'E': 7.1,
    'F': 3.5,
    'G': 0
}

def astar(start, goal):
    open_list = [(h[start], 0, start, [start])]
    visited = set()

    while open_list:
        open_list.sort()
        f, g, node, path = open_list.pop(0)

        if node == goal:
            print("Path:", " -> ".join(path))
            print("Cost:", g)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + h[neighbor]
                open_list.append((new_f, new_g, neighbor,
                                  path + [neighbor]))

    print("No path found")

astar('S', 'G')
