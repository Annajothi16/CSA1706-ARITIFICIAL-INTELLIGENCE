graph = {
    'P': ['R', 'C', 'F'],
    'C': ['R', 'M', 'D'],
    'R': ['E'],
    'F': ['M'],
    'M': ['D', 'L'],
    'E': ['D', 'S'],
    'D': ['S', 'N'],
    'L': ['N'],
    'N': ['S'],
    'S': []
}

h = {
    'P': 10,
    'R': 8,
    'C': 6,
    'F': 11,
    'M': 9,
    'E': 3,
    'D': 4,
    'L': 9,
    'N': 10,
    'S': 0
}

def greedy(start, goal):
    open_list = [start]
    visited = set()
    parent = {}

    while open_list:
        open_list.sort(key=lambda x: h[x])
        node = open_list.pop(0)

        if node in visited:
            continue

        visited.add(node)
        print(node, end=" ")

        if node == goal:
            path = []
            while node in parent:
                path.append(node)
                node = parent[node]
            path.append(start)
            path.reverse()
            print("\nPath:", " -> ".join(path))
            return

        for neighbor in graph[node]:
            if neighbor not in visited and neighbor not in parent:
                parent[neighbor] = node
                open_list.append(neighbor)

    print("\nGoal not found")

greedy('P', 'S')
