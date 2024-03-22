import numpy as np
from pymoo.indicators.gd import GD
from pymoo.indicators.gd_plus import GDPlus
from pymoo.indicators.igd import IGD
from pymoo.indicators.igd_plus import IGDPlus
from pymoo.indicators.hv import HV

def calculate_hypervolume(pareto_front, reference_point):
    hv = HV(ref_point=reference_point)
    return hv(pareto_front)

def calculate_gd(pareto_front, reference_front):
    gd = GD(reference_front)
    return gd(pareto_front)

def calculate_gd_plus(pareto_front, reference_front):
    gd_plus = GDPlus(reference_front)
    return gd_plus(pareto_front)

def calculate_igd(pareto_front, reference_front):
    igd = IGD(reference_front)
    return igd(pareto_front)

def calculate_igd_plus(pareto_front, reference_front):
    igd_plus = IGDPlus(reference_front)
    return igd_plus(pareto_front)

def calculate_spread(pareto_front):
    extreme_solutions = np.zeros((len(pareto_front[0]), len(pareto_front[0])))
    for i in range(len(pareto_front[0])):
        min_val = np.min(pareto_front[:, i])
        max_val = np.max(pareto_front[:, i])
        extreme_solutions[i] = np.array([min_val if j == i else max_val for j in range(len(pareto_front[0]))])

    distances = np.linalg.norm(pareto_front - extreme_solutions, axis=1)
    d_mean = np.mean(distances)
    d_std = np.std(distances)

    return np.sqrt(np.sum((distances - d_mean) ** 2)) / (len(pareto_front) - 1)

def calculate_diversity(pareto_front):
    diversity = 0.0
    for i in range(len(pareto_front)):
        for j in range(i+1, len(pareto_front)):
            diversity += np.linalg.norm(pareto_front[i] - pareto_front[j])
    return diversity / (len(pareto_front) * (len(pareto_front) - 1) / 2)

def calculate_convergence_speed(pareto_fronts):
    convergence_speed = []
    for i in range(1, len(pareto_fronts)):
        prev_front = pareto_fronts[i-1]
        current_front = pareto_fronts[i]
        min_distances = np.min(np.linalg.norm(prev_front[:, np.newaxis] - current_front, axis=2), axis=1)
        convergence_speed.append(np.mean(min_distances))
    return convergence_speed

def generate_performance_metrics_table(pareto_front, reference_point, reference_front):
    hypervolume = calculate_hypervolume(pareto_front, reference_point)
    gd = calculate_gd(pareto_front, reference_front)
    gd_plus = calculate_gd_plus(pareto_front, reference_front)
    igd = calculate_igd(pareto_front, reference_front)
    igd_plus = calculate_igd_plus(pareto_front, reference_front)
    spread = calculate_spread(pareto_front)
    diversity = calculate_diversity(pareto_front)
    convergence_speed = calculate_convergence_speed([pareto_front])
    
    table = """
    Performans Metrikleri:
    - Hiper-hacim: {}
    - Generational Distance (GD): {}
    - Generational Distance Plus (GD+): {}
    - Inverted Generational Distance (IGD): {}
    - Inverted Generational Distance Plus (IGD+): {}
    - Genişlik: {}
    - Çeşitlilik: {}
    - Yakınsama hızı: {}
    """.format(hypervolume, gd, gd_plus, igd, igd_plus, spread, diversity, convergence_speed)
    
    return table

def generate_pareto_front_comparison_table(pareto_front_mopso, pareto_front_ga):
    num_solutions_mopso = len(pareto_front_mopso)
    num_solutions_ga = len(pareto_front_ga)
    combined_pareto_front = np.vstack((pareto_front_mopso, pareto_front_ga))
    
    dominance_analysis = compare_pareto_fronts(pareto_front_mopso, pareto_front_ga)
    
    table = """
    Pareto Cephesi Karşılaştırma:
    - MOPSO Pareto cephesindeki çözüm sayısı: {}
    - GA Pareto cephesindeki çözüm sayısı: {}
    - Birleştirilmiş Pareto cephesi: {}
    - Baskınlık ilişkileri analizi: {}
    """.format(num_solutions_mopso, num_solutions_ga, combined_pareto_front, dominance_analysis)
    
    return table

def compare_pareto_fronts(pareto_front_1, pareto_front_2):
    dominance_matrix = np.zeros((len(pareto_front_1), len(pareto_front_2)))
    for i in range(len(pareto_front_1)):
        for j in range(len(pareto_front_2)):
            if np.all(pareto_front_1[i] <= pareto_front_2[j]) and np.any(pareto_front_1[i] < pareto_front_2[j]):
                dominance_matrix[i, j] = 1
            elif np.all(pareto_front_2[j] <= pareto_front_1[i]) and np.any(pareto_front_2[j] < pareto_front_1[i]):
                dominance_matrix[i, j] = -1
    
    analysis = """
    Baskınlık Matrisi:
    {}
    
    Baskınlık İlişkileri Özeti:
    - MOPSO baskın çözüm sayısı: {}
    - GA baskın çözüm sayısı: {}
    - Baskınlık yok (eşit) çözüm sayısı: {}
    """.format(dominance_matrix,
               np.sum(dominance_matrix == 1),
               np.sum(dominance_matrix == -1),
               np.sum(dominance_matrix == 0))
    
    return analysis

def generate_objective_function_values_table(objective_values_mopso, objective_values_ga):
    best_values_mopso = np.min(objective_values_mopso, axis=0)
    mean_values_mopso = np.mean(objective_values_mopso, axis=0)
    worst_values_mopso = np.max(objective_values_mopso, axis=0)
    
    best_values_ga = np.min(objective_values_ga, axis=0)
    mean_values_ga = np.mean(objective_values_ga, axis=0)
    worst_values_ga = np.max(objective_values_ga, axis=0)
    
    tradeoff_analysis = analyze_tradeoffs(objective_values_mopso, objective_values_ga)
    
    table = """
    Objektif Fonksiyon Değerleri:
    - MOPSO:
      - En iyi değerler: {}
      - Ortalama değerler: {}
      - En kötü değerler: {}
    - GA:
      - En iyi değerler: {}
      - Ortalama değerler: {}
      - En kötü değerler: {}
    - Objektif fonksiyonlar arasındaki ödünleşmelerin analizi: {}
    """.format(best_values_mopso, mean_values_mopso, worst_values_mopso,
               best_values_ga, mean_values_ga, worst_values_ga,
               tradeoff_analysis)
    
    return table

def analyze_tradeoffs(objective_values_1, objective_values_2):
    correlation_matrix = np.corrcoef(np.concatenate((objective_values_1, objective_values_2), axis=0).T)
    
    analysis = """
    Korelasyon Matrisi:
    {}
    
    Ödünleşme Analizi:
    - Pozitif korelasyon (ödünleşme yok) çiftleri: {}
    - Negatif korelasyon (ödünleşme var) çiftleri: {}
    """.format(correlation_matrix,
               np.sum(correlation_matrix > 0.5) - len(correlation_matrix),
               np.sum(correlation_matrix < -0.5))
    
    return analysis

def generate_computation_time_table(computation_time_mopso, computation_time_ga):
    total_time_mopso = np.sum(computation_time_mopso)
    mean_time_mopso = np.mean(computation_time_mopso)
    std_time_mopso = np.std(computation_time_mopso)
    
    total_time_ga = np.sum(computation_time_ga)
    mean_time_ga = np.mean(computation_time_ga)
    std_time_ga = np.std(computation_time_ga)
    
    table = """
    Hesaplama Süresi:
    - MOPSO:
      - Her test için geçen süre: {}
      - Ortalama süre: {}
      - Standart sapma: {}
      - Toplam süre: {}
    - GA:
      - Her test için geçen süre: {}
      - Ortalama süre: {}
      - Standart sapma: {}
      - Toplam süre: {}
    """.format(computation_time_mopso, mean_time_mopso, std_time_mopso, total_time_mopso,
               computation_time_ga, mean_time_ga, std_time_ga, total_time_ga)
    
    return table