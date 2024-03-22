import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_pareto_front_3d(pareto_front, objective_functions):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    if pareto_front.shape[0] > 0:
        ax.scatter(pareto_front[:, 0], pareto_front[:, 1], pareto_front[:, 2])
        ax.set_xlabel(objective_functions[0].__name__)
        ax.set_ylabel(objective_functions[1].__name__)
        ax.set_zlabel(objective_functions[2].__name__)
        ax.set_title("Pareto Front (3D)")
    else:
        ax.text(0.5, 0.5, 0.5, "No Pareto optimal solutions found.", ha='center', va='center')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_zlim(0, 1)
        
    plt.show()

def plot_parallel_coordinates(pareto_front, objective_functions, design_variable_names):
    fig, ax = plt.subplots(figsize=(10, 5))
    
    if pareto_front.shape[0] > 0:
        # Normalize data
        normalized_data = np.copy(pareto_front)
        for i in range(pareto_front.shape[1]):
            min_val = pareto_front[:, i].min()
            max_val = pareto_front[:, i].max()
            if max_val - min_val > 0:
                normalized_data[:, i] = (pareto_front[:, i] - min_val) / (max_val - min_val)
            else:
                normalized_data[:, i] = 0.5  # Tüm değerler eşitse, 0.5'e ayarla
        
        # Plot data
        for i in range(normalized_data.shape[0]):
            ax.plot(normalized_data[i, :], marker='o', markersize=5, alpha=0.7)
        
        # Set labels
        ax.set_xticks(range(len(objective_functions) + len(design_variable_names)))
        ax.set_xticklabels(list(map(lambda x: x.__name__, objective_functions)) + design_variable_names)
        ax.set_title("Parallel Coordinates Plot")
    else:
        ax.text(0.5, 0.5, "No Pareto optimal solutions found.", ha='center', va='center')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        
    plt.tight_layout()
    plt.show()

def plot_radar_chart(pareto_front, objective_functions):
    if pareto_front.shape[0] > 0:
        # Normalize data
        normalized_data = np.copy(pareto_front)
        for i in range(pareto_front.shape[1]):
            min_val = pareto_front[:, i].min()
            max_val = pareto_front[:, i].max()
            if max_val - min_val > 0:
                normalized_data[:, i] = (pareto_front[:, i] - min_val) / (max_val - min_val)
            else:
                normalized_data[:, i] = 0.5

        # Create radar chart
        fig = plt.figure(figsize=(6, 6))
        ax = fig.add_subplot(111, polar=True)

        # Set number of objectives as number of axes
        angles = np.linspace(0, 2*np.pi, len(objective_functions), endpoint=False)
        angles = np.concatenate((angles, [angles[0]]))  # Closed polygon
        ax.set_thetagrids(np.degrees(angles[:-1]), labels=list(map(lambda x: x.__name__, objective_functions)))

        for i in range(normalized_data.shape[0]):
            values = np.concatenate((normalized_data[i, :], [normalized_data[i, 0]]))
            ax.plot(angles, values, marker='o', markersize=5, alpha=0.7)
            ax.fill(angles, values, alpha=0.1)

        ax.set_title("Radar Chart")
    else:
        plt.text(0.5, 0.5, "No Pareto optimal solutions found.", ha='center', va='center')

    plt.tight_layout()
    plt.show()
    
def plot_heatmap(pareto_front, objective_functions, design_variable_names):
    if pareto_front.shape[0] > 0:
        fig, ax = plt.subplots(figsize=(8, 6))
        im = ax.imshow(pareto_front, cmap='viridis', aspect='auto')

        xlabels = list(map(lambda x: x.__name__, objective_functions)) + design_variable_names
        ax.set_xticks(np.arange(len(xlabels)))
        ax.set_xticklabels(xlabels, rotation=45, ha='right')
        ax.set_yticks(np.arange(pareto_front.shape[0]))
        ax.set_yticklabels(np.arange(1, pareto_front.shape[0]+1))

        ax.set_xlabel('Objectives and Design Variables')
        ax.set_ylabel('Solution Index')
        ax.set_title('Heatmap of Pareto Front')

        fig.colorbar(im)
    else:
        plt.text(0.5, 0.5, "No Pareto optimal solutions found.", ha='center', va='center')

    plt.tight_layout()
    plt.show()