import unittest
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.optimization_functions import thrust_objective, sfc_objective, weight_objective, cost_objective, evaluate_constraints
from utils.data_processing import load_data, preprocess_data

class TestOptimizationFunctions(unittest.TestCase):
    def setUp(self):
        self.particle = np.array([150, 75, 0.3, 80])
        engine_data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cfm56_7b_data.json')
        material_properties_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'material_properties.json')
        engine_data = load_data(engine_data_path)
        material_properties = load_data(material_properties_path)
        self.data = preprocess_data(engine_data, material_properties)

    def test_thrust_objective(self):
        result = thrust_objective(self.particle, self.data)
        self.assertIsInstance(result, float)

    def test_sfc_objective(self):
        result = sfc_objective(self.particle, self.data)
        self.assertIsInstance(result, float)

    def test_weight_objective(self):
        result = weight_objective(self.particle, self.data)
        self.assertIsInstance(result, float)

    def test_cost_objective(self):
        result = cost_objective(self.particle, self.data)
        self.assertIsInstance(result, float)

    def test_evaluate_constraints(self):
        constraints = evaluate_constraints(self.particle, self.data)
        self.assertIsInstance(constraints, list)
        self.assertEqual(len(constraints), 4)

if __name__ == "__main__":
    unittest.main()