# Graph Coloring using Python

graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'F'],
    'D': ['A', 'E', 'G'],
    'E': ['B', 'D', 'F', 'G', 'H'],
    'F': ['C', 'E', 'I'],
    'G': ['D', 'E', 'H'],
    'H': ['G', 'E', 'I'],
    'I': ['F', 'H']
}

colors = ['Red', 'Green', 'Blue']

result = {}

for region in graph:
    used = [result[n] for n in graph[region] if n in result]

    for color in colors:
        if color not in used:
            result[region] = color
            break

print("Map Coloring:")
for region, color in result.items():
    print(region, ":", color)
