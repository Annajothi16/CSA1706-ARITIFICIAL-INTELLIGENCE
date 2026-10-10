from collections import deque

capacity = (12, 8, 5)
start = (12, 0, 0)
target = 6

queue = deque([start])
parent = {start: None}

while queue:
    state = queue.popleft()

    if state[1] == target:
        path = []

        while state is not None:
            path.append(state)
            state = parent[state]

        path.reverse()

        print("12L  8L  5L")
        for a, b, c in path:
            print(a, " ", b, " ", c)
        break

    for i in range(3):
        for j in range(3):
            if i == j:
                continue

            amount = min(state[i], capacity[j] - state[j])

            if amount > 0:
                new_state = list(state)
                new_state[i] -= amount
                new_state[j] += amount
                new_state = tuple(new_state)

                if new_state not in parent:
                    parent[new_state] = state
                    queue.append(new_state)
else:
    print("Target not possible")
