import numpy as np
import time
from models.mopso import MOPSO
from utils.data_processing import load_data, preprocess_data
from utils.optimization_functions import thrust_objective, sfc_objective, weight_objective, cost_objective, evaluate_constraints
from utils.visualization import plot_pareto_front_3d, plot_parallel_coordinates, plot_radar_chart, plot_heatmap
from models.genetic_algorithm import GeneticAlgorithm
from utils.reporting import generate_performance_metrics_table, generate_pareto_front_comparison_table, generate_objective_function_values_table, generate_computation_time_table
import logging

def main():
    # Loglama yapılandırması
    logging.basicConfig(filename='optimization.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

    # Verileri yükle ve ön işleme yap
    engine_data = load_data("data/cfm56_7b_data.json")
    material_properties = load_data("data/material_properties.json")
    data = preprocess_data(engine_data, material_properties)

    # MOPSO parametrelerini ayarla
    objective_functions = [thrust_objective, sfc_objective, weight_objective, cost_objective]
    constraints = [evaluate_constraints]
    design_variables = data["design_variables"]
    population_size = 100
    max_iterations = 50

    # MOPSO örneğini oluştur ve optimizasyonu çalıştır
    mopso = MOPSO(objective_functions, constraints, design_variables, population_size, max_iterations, data)
    start_time_mopso = time.time()
    pareto_front_mopso = mopso.optimize()
    computation_time_mopso = time.time() - start_time_mopso
    objective_values_mopso = np.array([[objective(point, data) for objective in objective_functions] for point in pareto_front_mopso])

    # Genetik Algoritma örneğini oluştur ve optimizasyonu çalıştır
    ga = GeneticAlgorithm(objective_functions, constraints, design_variables, population_size, max_iterations, data)
    start_time_ga = time.time()
    pareto_front_ga = ga.optimize()
    computation_time_ga = time.time() - start_time_ga
    objective_values_ga = np.array([[objective(point, data) for objective in objective_functions] for point in pareto_front_ga])

    # Pareto cephelerini birleştir
    pareto_front = np.vstack((pareto_front_mopso, pareto_front_ga))
    pareto_front = pareto_front[np.all(~(pareto_front[:, None] > pareto_front), axis=2).any(axis=1)]

    # Sonuçları logla
    logging.info(f"Pareto Front: {pareto_front}")
    if pareto_front.shape[0] > 0:
        logging.info(f"Objective Function Values: {[objective(pareto_front[0], data) for objective in objective_functions]}")
    else:
        logging.info("No Pareto optimal solutions found.")

    # Raporlama
    reference_point = np.max(pareto_front, axis=0)
    reference_front = pareto_front  # Referans cepheyi Pareto cephesi olarak ayarla
    
    performance_metrics_table = generate_performance_metrics_table(pareto_front, reference_point, reference_front)
    pareto_front_comparison_table = generate_pareto_front_comparison_table(pareto_front_mopso, pareto_front_ga)
    
    if objective_values_mopso.size > 0 and objective_values_ga.size > 0:
        objective_function_values_table = generate_objective_function_values_table(objective_values_mopso, objective_values_ga)
    else:
        objective_function_values_table = "Objektif fonksiyon değerleri bulunamadı."
    
    computation_time_table = generate_computation_time_table([computation_time_mopso], [computation_time_ga])
    
    # Tabloları results klasörüne UTF-8 kodlamasıyla kaydet
    with open("results/performance_metrics.txt", "w", encoding="utf-8") as file:
        file.write(performance_metrics_table)

    with open("results/pareto_front_comparison.txt", "w", encoding="utf-8") as file:
        file.write(pareto_front_comparison_table)

    with open("results/objective_function_values.txt", "w", encoding="utf-8") as file:
        file.write(objective_function_values_table)

    with open("results/computation_time.txt", "w", encoding="utf-8") as file:
        file.write(computation_time_table)

    # Sonuçları görselleştir
    plot_pareto_front_3d(pareto_front, objective_functions)
    plot_parallel_coordinates(pareto_front, objective_functions, design_variables['names'])
    plot_radar_chart(pareto_front, objective_functions)
    plot_heatmap(pareto_front, objective_functions, design_variables['names'])

if __name__ == "__main__":
    main()