from collections import deque

def water_jug():
    capacity = (8, 5, 3)
    start = (8, 0, 0)
    target = (4, 4, 0)

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == target:
            print("Solution:")
            for step in path:
                print(step)
            return

        for i in range(3):
            for j in range(3):
                if i != j:
                    new_state = list(state)
                    amount = min(state[i], capacity[j] - state[j])

                    new_state[i] -= amount
                    new_state[j] += amount
                    new_state = tuple(new_state)

                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, path + [new_state]))

    print("No solution found")

water_jug()
