import unittest
from jet_engine_optimization.utils.data_processing import load_data, preprocess_data
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.data_processing import load_data, preprocess_data

class TestDataProcessing(unittest.TestCase):
    def test_load_data(self):
        data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cfm56_7b_data.json')
        data = load_data(data_path)
        self.assertIsInstance(data, dict)
        self.assertIn("engine_name", data)
        self.assertIn("design_variables", data)

    def test_preprocess_data(self):
        engine_data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cfm56_7b_data.json')
        material_properties_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'material_properties.json')
        engine_data = load_data(engine_data_path)
        material_properties = load_data(material_properties_path)
        data = preprocess_data(engine_data, material_properties)
        self.assertIsInstance(data, dict)
        self.assertIn("engine_data", data)
        self.assertIn("material_properties", data)
        self.assertIn("design_variables", data)
        self.assertIn("names", data["design_variables"])
        self.assertIn("bounds", data["design_variables"])

if __name__ == "__main__":
    unittest.main()