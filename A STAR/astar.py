graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 3},
    'C': {'E': 5},
    'D': {'F': 2, 'G': 4},
    'E': {'G': 3},
    'F': {'G': 1},
    'G': {}
}

h = {
    'A': 5,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 1,
    'G': 0
}

def astar(start, goal):
    open_list = [(h[start], 0, start, [start])]
    closed = set()

    while open_list:
        open_list.sort()
        f, g, node, path = open_list.pop(0)

        if node == goal:
            print("Path:", " -> ".join(path))
            print("Cost:", g)
            return

        if node in closed:
            continue

        closed.add(node)

        for next_node, cost in graph[node].items():
            if next_node not in closed:
                new_g = g + cost
                new_f = new_g + h[next_node]
                open_list.append(
                    (new_f, new_g, next_node, path + [next_node])
                )

    print("No path found")

astar('A', 'G')
