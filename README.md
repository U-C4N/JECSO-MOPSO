# JECSO-MOPSO

JECSO-MOPSO (Jet Engine Component Sizing Optimization using Multi-Objective Particle Swarm Optimization) is a novel optimization algorithm specifically designed for the multi-objective optimization of jet engine components. This repository contains the implementation of JECSO-MOPSO in Python, along with sample test problems and a real-world jet engine design case study.

## Features

JECSO-MOPSO adapts and enhances the standard Multi-Objective Particle Swarm Optimization (MOPSO) algorithm to address the specific requirements of jet engine design optimization. The algorithm incorporates the following key features:

1. **Adapted velocity and position update equations:** JECSO-MOPSO modifies the standard MOPSO equations to consider the physical properties of jet engine components, enabling more effective exploration of the design space.

2. **Local search strategy:** A local search procedure is employed to improve solutions on the Pareto front, enhancing the convergence and diversity of the optimization process.

3. **Specialized constraint handling mechanism:** JECSO-MOPSO includes a tailored constraint handling technique that efficiently deals with the complex constraints encountered in jet engine design, ensuring feasible and high-quality solutions.

## Installation

To use JECSO-MOPSO, follow these steps:

1. Clone the repository:
  ```bash
  git clone https://github.com/your-username/JECSO-MOPSO.git
Install the required dependencies:
bash


Copy code
pip install -r requirements.txt
Usage
The repository provides a user-friendly interface to run the JECSO-MOPSO algorithm on various optimization problems. Here's a basic example:

python


Copy code
from jecso_mopso import JECSO_MOPSO

# Define the optimization problem
problem = YourOptimizationProblem()

# Set the algorithm parameters
max_iterations = 100
population_size = 50
# ...

# Create an instance of JECSO-MOPSO
optimizer = JECSO_MOPSO(problem, max_iterations, population_size, ...)

# Run the optimization
pareto_front = optimizer.optimize()

# Visualize the results
optimizer.plot_pareto_front()
For more detailed usage instructions and examples, please refer to the documentation.

Test Problems
The repository includes several benchmark test problems to evaluate the performance of JECSO-MOPSO:

ZDT1: A bi-objective test problem with 30 decision variables.
DTLZ2: A scalable test problem with a configurable number of objectives.
Jet Engine Design Problem: A real-world case study of optimizing the component sizes of a turbofan engine.
These test problems can be found in the test_problems directory.
