import numpy as np

class MOPSO:
    def __init__(self, objective_functions, constraints, design_variables, population_size, max_iterations, data):
        self.objective_functions = objective_functions
        self.constraints = constraints
        self.design_variables = design_variables
        self.population_size = population_size
        self.max_iterations = max_iterations
        self.data = data
        self.inertia_weight = 0.7298
        self.cognitive_weight = 1.49618
        self.social_weight = 1.49618
        self.local_search_probability = 0.1
        self.adaptive_inertia_weight = True

    def optimize(self):
        print("Starting MOPSO optimization...")

        # Parçacık sürüsünü başlat
        swarm = np.array([np.random.uniform(bounds[0], bounds[1], self.population_size) for bounds in self.design_variables['bounds']]).T

        # Parçacıkların en iyi pozisyonlarını ve global en iyi pozisyonu başlat
        personal_best_positions = swarm.copy()
        personal_best_scores = np.full((self.population_size, len(self.objective_functions)), np.inf)
        pareto_front = np.empty((0, len(self.objective_functions)))

        for iteration in range(self.max_iterations):
            print(f"Iteration {iteration + 1}/{self.max_iterations}")

            # Parçacıkları değerlendir
            for i, particle in enumerate(swarm):
                # Amaç fonksiyonlarını hesapla
                scores = np.array([objective(particle, self.data) for objective in self.objective_functions])

                # Kısıtlamaları kontrol et
                constraints = np.array(self.constraints[0](particle, self.data))
                if np.any(constraints > 0):
                    continue

                # Parçacığın en iyi pozisyonunu güncelle
                if np.sum(scores) < np.sum(personal_best_scores[i]):
                    personal_best_positions[i] = particle
                    personal_best_scores[i] = scores

                # Pareto cephesini güncelle
                if np.all(scores <= pareto_front, axis=1).any() and not np.all(scores == pareto_front, axis=1).any():
                    pareto_front = np.vstack((pareto_front, scores))
                    pareto_front = pareto_front[np.all(~(pareto_front[:, None] > pareto_front), axis=2).any(axis=1)]
                elif pareto_front.shape[0] == 0:
                    pareto_front = np.vstack((pareto_front, scores))

            # Parçacıkları güncelle
            for i, particle in enumerate(swarm):
                # Hız güncelleme
                if pareto_front.shape[0] > 0:
                    best_index = np.random.randint(pareto_front.shape[0])
                    best_particle = personal_best_positions[np.random.randint(self.population_size)]
                else:
                    best_particle = personal_best_positions[i]

                if self.adaptive_inertia_weight:
                    self.inertia_weight = 0.5 * (1 + np.random.rand())

                velocity = self.inertia_weight * (particle - personal_best_positions[i]) + \
                           self.cognitive_weight * np.random.rand(particle.shape[0]) * (personal_best_positions[i] - particle) + \
                           self.social_weight * np.random.rand(particle.shape[0]) * (best_particle - particle)

                # Pozisyon güncelleme
                particle += velocity

                # Sınırları kontrol et
                for j, bounds in enumerate(self.design_variables['bounds']):
                    particle[j] = np.clip(particle[j], bounds[0], bounds[1])

            # Yerel arama uygula
            if np.random.rand() < self.local_search_probability:
                self.local_search(swarm, pareto_front)

        print("MOPSO optimization completed.")
        return pareto_front

    def local_search(self, swarm, pareto_front):
        for i in range(swarm.shape[0]):
            if np.random.rand() < 0.5:
                particle = swarm[i]
                best_particle = pareto_front[np.random.randint(pareto_front.shape[0])]
                particle = particle + 0.5 * np.random.rand(particle.shape[0]) * (best_particle - particle)
                swarm[i] = particle