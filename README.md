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
