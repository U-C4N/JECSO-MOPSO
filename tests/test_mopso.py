import unittest
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.mopso import MOPSO
from utils.optimization_functions import thrust_objective, sfc_objective, weight_objective, cost_objective, evaluate_constraints

class TestMOPSO(unittest.TestCase):
    def test_optimize(self):
        objective_functions = [thrust_objective, sfc_objective, weight_objective, cost_objective]
        constraints = [evaluate_constraints]
        design_variables = {"names": ["fan_diameter", "compressor_diameter", "combustion_chamber_volume", "turbine_diameter"],
                            "bounds": [(100, 200), (50, 100), (0.1, 0.5), (50, 100)]}
        population_size = 10
        max_iterations = 5
        data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cfm56_7b_data.json')
        data = {"engine_data": data_path, "material_properties": {}}

        mopso = MOPSO(objective_functions, constraints, design_variables, population_size, max_iterations, data)
        pareto_front = mopso.optimize()

        self.assertIsInstance(pareto_front, np.ndarray)
        self.assertGreater(pareto_front.shape[0], 0)
        self.assertEqual(pareto_front.shape[1], len(objective_functions))

if __name__ == "__main__":
    unittest.main()