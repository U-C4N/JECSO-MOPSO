import unittest
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.visualization import plot_pareto_front, plot_objective_values, plot_design_variables

class TestVisualization(unittest.TestCase):
    def test_plot_pareto_front(self):
        pareto_front = np.array([[1, 2], [2, 1], [1.5, 1.5]])
        objective_functions = [lambda x, y: x, lambda x, y: y]
        plot_pareto_front(pareto_front, objective_functions)

    def test_plot_objective_values(self):
        pareto_front = np.array([[1, 2], [2, 1], [1.5, 1.5]])
        objective_functions = [lambda x, y: x, lambda x, y: y]
        plot_objective_values(pareto_front, objective_functions)

    def test_plot_design_variables(self):
        pareto_front = np.array([[1, 2], [2, 1], [1.5, 1.5]])
        design_variable_names = ["var1", "var2"]
        plot_design_variables(pareto_front, design_variable_names)

if __name__ == "__main__":
    unittest.main()