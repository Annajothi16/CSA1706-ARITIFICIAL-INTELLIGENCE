1) BFS:
BEGIN
1. Add the start node to the QUEUE.
2. Mark the start node as visited.
3. WHILE QUEUE is not empty:
      a. Remove the front node.
      b. If it is the goal, return SUCCESS.
      c. For each unvisited neighbour:
            Mark it as visited.
            Add it to the QUEUE.
4. Return FAILURE.
END

2) DFS:

BEGIN
1. Push the start node onto the STACK.
2. WHILE STACK is not empty:
      a. Pop a node from the STACK.
      b. If it is the goal, return SUCCESS.
      c. If it is not visited:
            Mark it as visited.
            Push its unvisited neighbours.
3. Return FAILURE.
END

3) UCS:

BEGIN
1. Add the start node to the PRIORITY QUEUE
   with cost 0.
2. WHILE PRIORITY QUEUE is not empty:
      a. Remove the node with the lowest cost.
      b. If it is the goal, return the path and cost.
      c. For each neighbour:
            Calculate the new path cost.
            If the cost is lower than the known cost:
                Update the cost and parent.
                Add the neighbour to the queue.
3. Return FAILURE.
END

4) Water jug:

BEGIN
1. Initialize both jugs to 0.
2. Add the initial state to the QUEUE.
3. WHILE QUEUE is not empty:
      a. Remove a state (x, y).
      b. If x or y equals the target:
            Return SUCCESS.
      c. Generate new states by:
            i.   Filling Jug A.
            ii.  Filling Jug B.
            iii. Emptying Jug A.
            iv.  Emptying Jug B.
            v.   Pouring A into B.
            vi.  Pouring B into A.
      d. Add each unvisited state to the QUEUE.
4. Return FAILURE if no solution exists.
END

5) A star Algorithm:

BEGIN
1. Add the start node to OPEN.
2. WHILE OPEN is not empty:
   a. Select node with lowest f(n).
   b. If node is the goal, return path.
   c. Move node to CLOSED.
   d. For each neighbour:
      Calculate g(n).
      Calculate f(n) = g(n) + h(n).
      Update cost and parent if better.
      Add neighbour to OPEN if needed.
3. Return failure.
END

6) GBFS Algorithm:

BEGIN
1. Add the start node to OPEN.
2. WHILE OPEN is not empty:
   a. Select node with lowest h(n).
   b. If node is the goal, return path.
   c. Move node to CLOSED.
   d. Add unexplored neighbours to OPEN.
      Store their heuristic values and parents.
3. Return failure.
END

7) Mini Max Algorithm:

BEGIN
1. If node is terminal, return its value.
2. If node is MAX:
      best = -INFINITY
      For each child:
          best = MAX(best, MINIMAX(child))
      Return best.
3. Otherwise, node is MIN:
      best = +INFINITY
      For each child:
          best = MIN(best, MINIMAX(child))
      Return best.

END

8)Alpha Beta Pruning:

BEGIN
1. If node is terminal, return its value.
2. If node is MAX:
      best = -INFINITY
      For each child:
          best = MAX(best, ALPHA_BETA(child))
          alpha = MAX(alpha, best)
          If alpha >= beta, BREAK.
      Return best.
3. Otherwise, node is MIN:
      best = +INFINITY
      For each child:
          best = MIN(best, ALPHA_BETA(child))
          beta = MIN(beta, best)
          If alpha >= beta, BREAK.
      Return best.
END

9) N Queens:

BEGIN
1. Start with an empty chessboard.
2. Place one queen in each row.
3. For each column:
      Check whether the position is safe.
      If safe:
          Place the queen.
          Recursively solve the next row.
          If unsuccessful, remove the queen.
4. If all rows are filled, return SUCCESS.
5. Otherwise, return FAILURE.

END

10) Map Coloring:

BEGIN
1. Define regions, neighbours, and available colours.
2. Select an uncoloured region.
3. For each available colour:
      Check whether neighbouring regions
      have the same colour.
      If no conflict:
          Assign the colour.
          Recursively colour the remaining regions.
          If unsuccessful, remove the colour.
4. If all regions are coloured, return SUCCESS.
5. Otherwise, return FAILURE.
END


