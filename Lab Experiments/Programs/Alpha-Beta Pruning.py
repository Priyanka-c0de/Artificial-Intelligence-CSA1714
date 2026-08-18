import math

def alphabeta(depth, node_index, is_maximizing, values, alpha, beta):
    # Terminal node check (leaf nodes)
    if depth == 3:
        return values[node_index]

    if is_maximizing:
        best = -math.inf
        # Recur for left and right children
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha-Beta Pruning condition
            if beta <= alpha:
                print(f"Pruned remaining branches at depth {depth} (Maximizer)")
                break
        return best
    else:
        best = math.inf
        # Recur for left and right children
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha-Beta Pruning condition
            if beta <= alpha:
                print(f"Pruned remaining branches at depth {depth} (Minimizer)")
                break
        return best

# Leaf node values of a complete binary game tree (Depth 3)
leaf_values = [3, 5, 6, 9, 1, 2, 0, -1]

initial_alpha = -math.inf
initial_beta = math.inf

optimal_score = alphabeta(0, 0, True, leaf_values, initial_alpha, initial_beta)

print(f"\nOptimal score calculated by Alpha-Beta Pruning: {optimal_score}")