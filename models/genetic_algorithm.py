import numpy as np

class GeneticAlgorithm:
    def __init__(self, objective_functions, constraints, design_variables, population_size, max_iterations, data):
        self.objective_functions = objective_functions
        self.constraints = constraints
        self.design_variables = design_variables
        self.population_size = population_size
        self.max_iterations = max_iterations
        self.data = data
        self.mutation_rate = 0.1
        self.crossover_rate = 0.9

    def optimize(self):
        print("Starting GA optimization...")

        # Popülasyonu başlat
        population = np.array([np.random.uniform(bounds[0], bounds[1], self.population_size) for bounds in self.design_variables['bounds']]).T

        for iteration in range(self.max_iterations):
            print(f"Iteration {iteration + 1}/{self.max_iterations}")

            # Bireyleri değerlendir
            scores = np.array([self.evaluate(individual) for individual in population])

            # Pareto cephesini bul
            pareto_front = self.find_pareto_front(population, scores)

            # Yeni nesil oluştur
            new_population = []
            while len(new_population) < self.population_size:
                parent1, parent2 = self.select_parents(population, scores)
                child1, child2 = self.crossover(parent1, parent2)
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                new_population.extend([child1, child2])
            population = np.array(new_population)

        print("GA optimization completed.")
        return pareto_front

    def evaluate(self, individual):
        scores = np.array([objective(individual, self.data) for objective in self.objective_functions])
        constraints = np.array(self.constraints[0](individual, self.data))
        if np.any(constraints > 0):
            scores = np.full_like(scores, np.inf)
        return scores

    def find_pareto_front(self, population, scores):
        pareto_front = np.empty((0, len(self.objective_functions)))
        for i in range(scores.shape[0]):
            if np.all(scores[i] <= scores, axis=1).any() and not np.all(scores[i] == scores, axis=1).any():
                pareto_front = np.vstack((pareto_front, scores[i]))
                pareto_front = pareto_front[np.all(~(pareto_front[:, None] > pareto_front), axis=2).any(axis=1)]
        return pareto_front

    def select_parents(self, population, scores):
        fitnesses = 1 / np.sum(scores, axis=1)
        probabilities = fitnesses / np.sum(fitnesses)
        indices = np.random.choice(range(len(population)), size=2, p=probabilities)
        return population[indices]

    def crossover(self, parent1, parent2):
        if np.random.rand() < self.crossover_rate:
            crossover_point = np.random.randint(1, len(parent1))
            child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
            child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
            return child1, child2
        else:
            return parent1, parent2

    def mutate(self, individual):
        if np.random.rand() < self.mutation_rate:
            mutation_point = np.random.randint(len(individual))
            individual[mutation_point] = np.random.uniform(self.design_variables['bounds'][mutation_point][0],
                                                           self.design_variables['bounds'][mutation_point][1])
        return individual