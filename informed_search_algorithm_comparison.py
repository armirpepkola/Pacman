import matplotlib.pyplot as plt
import time

# Placeholder functions to simulate the informed search algorithms. These will track the metrics.
def simulate_astar():
    start_time = time.time()
    nodes_expanded = 200  # Example node count for A*
    path_length = 30  # Example path length for A*
    elapsed_time = time.time() - start_time + 0.15  # Example time adjustment for A*
    is_optimal = True  # A* guarantees optimality with an admissible heuristic
    return elapsed_time, nodes_expanded, path_length, is_optimal

def simulate_greedy():
    start_time = time.time()
    nodes_expanded = 250  # Example node count for Greedy
    path_length = 35  # Example path length for Greedy
    elapsed_time = time.time() - start_time + 0.10  # Example time adjustment for Greedy
    is_optimal = False  # Greedy does not guarantee optimality
    return elapsed_time, nodes_expanded, path_length, is_optimal

def simulate_advanced_greedy():
    start_time = time.time()
    nodes_expanded = 180  # Example node count for Advanced Greedy
    path_length = 33  # Example path length for Advanced Greedy
    elapsed_time = time.time() - start_time + 0.12  # Example time adjustment for Advanced Greedy
    is_optimal = False  # Advanced Greedy does not guarantee optimality
    return elapsed_time, nodes_expanded, path_length, is_optimal

# Collecting data from simulations
astar_data = simulate_astar()
greedy_data = simulate_greedy()
advanced_greedy_data = simulate_advanced_greedy()

# Extracting data for visualization
algorithms = ['A* Search', 'Greedy Search', 'Advanced Greedy']
execution_times = [astar_data[0], greedy_data[0], advanced_greedy_data[0]]
nodes_expanded = [astar_data[1], greedy_data[1], advanced_greedy_data[1]]
path_lengths = [astar_data[2], greedy_data[2], advanced_greedy_data[2]]
optimality = ['Yes', 'No', 'No']

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Execution Time
axs[0, 0].bar(algorithms, execution_times, color='blue')
axs[0, 0].set_title('Execution Time (s)')
axs[0, 0].set_ylabel('Time (s)')

# Nodes Expanded
axs[0, 1].bar(algorithms, nodes_expanded, color='green')
axs[0, 1].set_title('Nodes Expanded')
axs[0, 1].set_ylabel('Nodes')

# Path Length
axs[1, 0].bar(algorithms, path_lengths, color='red')
axs[1, 0].set_title('Path Length (Cost)')
axs[1, 0].set_ylabel('Length (Moves)')

# Optimality
axs[1, 1].bar(algorithms, optimality, color='purple')
axs[1, 1].set_title('Optimality of Solution')
axs[1, 1].set_ylabel('Is Optimal?')

plt.tight_layout()
plt.show()