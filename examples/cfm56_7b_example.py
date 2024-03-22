import sys
import os


# Proje dizininin kökünü Python'un modül arama yoluna ekle
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

from models.mopso import MOPSO
from utils.optimization_functions import thrust_objective, sfc_objective, weight_objective, cost_objective, evaluate_constraints
from utils.data_processing import load_data, preprocess_data
from utils.visualization import plot_pareto_front, plot_objective_values, plot_design_variables

def main():
    # Verileri yükle
    engine_data = load_data("../data/cfm56_7b_data.json")
    material_properties = load_data("../data/material_properties.json")
    data = preprocess_data(engine_data, material_properties)

    # MOPSO parametrelerini ayarla
    objective_functions = [thrust_objective, sfc_objective, weight_objective, cost_objective]
    constraints = [evaluate_constraints]
    design_variables = data["design_variables"]
    population_size = 100
    max_iterations = 500

    # MOPSO örneğini oluştur
    mopso = MOPSO(objective_functions, constraints, design_variables, population_size, max_iterations, data)

    # Optimizasyonu gerçekleştir
    pareto_front = mopso.optimize()

    # Sonuçları görselleştir ve analiz et
    plot_pareto_front(pareto_front, objective_functions)
    plot_objective_values(pareto_front, objective_functions)
    plot_design_variables(pareto_front, design_variables['names'])

if __name__ == "__main__":
    main()