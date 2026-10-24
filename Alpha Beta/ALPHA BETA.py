
def alpha_beta(node, depth, alpha, beta, maximizing):
    if depth == 0:
        return node

    if maximizing:
        best = -float('inf')
        for child in node:
            value = alpha_beta(child, depth - 1,
                               alpha, beta, False)
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break
        return best

    else:
        best = float('inf')
        for child in node:
            value = alpha_beta(child, depth - 1,
                               alpha, beta, True)
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break
        return best


tree = [
    [[2, 3], [5, 9]],
    [[0, 1], [7, 5]]
]

result = alpha_beta(tree, 3, -float('inf'),
                    float('inf'), True)

print("Optimal value:", result)
