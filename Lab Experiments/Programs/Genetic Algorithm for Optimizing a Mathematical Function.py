import random

# Fitness function
def fitness(x):
    return x ** 2

# Convert binary chromosome to decimal
def binary_to_decimal(binary):
    return int("".join(map(str, binary)), 2)

# Create initial population
population_size = 10
chromosome_length = 5

population = [
    [random.randint(0, 1) for _ in range(chromosome_length)]
    for _ in range(population_size)
]

# Genetic Algorithm
generations = 20

for generation in range(generations):

    # Calculate fitness
    fitness_values = [
        fitness(binary_to_decimal(chromosome))
        for chromosome in population
    ]

    # Select best two chromosomes
    selected = sorted(
        zip(population, fitness_values),
        key=lambda x: x[1],
        reverse=True
    )[:2]

    parent1 = selected[0][0]
    parent2 = selected[1][0]

    # Create new population
    new_population = [parent1, parent2]

    while len(new_population) < population_size:

        # Crossover
        point = random.randint(1, chromosome_length - 1)

        child = parent1[:point] + parent2[point:]

        # Mutation
        mutation_rate = 0.1

        for i in range(chromosome_length):
            if random.random() < mutation_rate:
                child[i] = 1 - child[i]

        new_population.append(child)

    population = new_population

# Find best solution
best = max(
    population,
    key=lambda chromosome: fitness(binary_to_decimal(chromosome))
)

best_x = binary_to_decimal(best)

print("Best Chromosome:", best)
print("Best Value of x:", best_x)
print("Maximum Fitness:", fitness(best_x))