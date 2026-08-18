def objective_function(x):
    # Mathematical function with a peak at x = 3, where f(3) = 15
    return -(x - 3) ** 2 + 15

def hill_climbing(start_x, step_size=0.1, max_iterations=1000):
    current_x = start_x
    current_score = objective_function(current_x)
    
    for _ in range(max_iterations):
        # Generate left and right neighbors
        neighbors = [current_x - step_size, current_x + step_size]
        
        # Find neighbor with best evaluation
        best_neighbor = max(neighbors, key=objective_function)
        best_neighbor_score = objective_function(best_neighbor)
        
        # Stop if no improvement can be made
        if best_neighbor_score <= current_score:
            break
            
        current_x = best_neighbor
        current_score = best_neighbor_score
        
    return current_x, current_score

# Starting search from x = 0.0
initial_x = 0.0
peak_x, peak_val = hill_climbing(initial_x)

print(f"Initial State x: {initial_x}")
print(f"Optimal State x found: {peak_x:.2f}")
print(f"Maximum Objective Value f(x): {peak_val:.2f}")