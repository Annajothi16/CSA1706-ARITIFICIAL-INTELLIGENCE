from collections import deque

def water_jug():
    capacity1 = 5
    capacity2 = 3
    target = 4

    queue = deque([(0, 0)])
    visited = set([(0, 0)])
    parent = {}

    while queue:
        a, b = queue.popleft()

        if a == target or b == target:
            path = []
            state = (a, b)

            while state in parent:
                path.append(state)
                state = parent[state]

            path.append((0, 0))
            path.reverse()

            for step in path:
                print("5L jug:", step[0], "| 3L jug:", step[1])
            return

        states = [
            (5, b),
            (a, 3),
            (0, b),
            (a, 0),
            (a - min(a, 3 - b), b + min(a, 3 - b)),
            (a + min(b, 5 - a), b - min(b, 5 - a))
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                parent[state] = (a, b)
                queue.append(state)

water_jug()
