# web3-squad-voodoo

## Overview

**web3-squad-voodoo** is a toolkit for leveraging the Active Inference framework to facilitate autopoietic team formation and maintenance in research and DAO (Decentralized Autonomous Organization) environments. The project provides methods to identify and assemble synergistic collaborators based on skill alignment and information-theoretic measures, such as variational free energy and KL divergence.

The core objective is to help find lab or DAO members for synergistic collaboration, using mathematical and probabilistic modeling to optimize team composition.

## Features
- **Active Inference for Team Formation**: Uses variational free energy minimization to match project needs with available skills.
- **Skill Alignment Analysis**: Quantifies how well individuals' skills align with project requirements.
- **Information-Theoretic Metrics**: Implements KL divergence and symmetry measures to assess compatibility and diversity.
- **Partner/Team Suggestion**: Identifies optimal collaborators or sub-squads within a DAO or research group.
- **Tutorial Notebook**: Step-by-step example for using the toolkit on real or synthetic data.

## Directory Structure
```
.
├── math/
│   ├── FEP.py         # Variational free energy and partner-finding logic
│   ├── spm.py         # Supporting mathematical and probabilistic functions
│   └── utils.py       # KL divergence and symmetry utilities
├── tutorial/
│   └── project_voodoo_tutorial.ipynb  # End-to-end usage tutorial
└── README.md
```

## Installation

This project relies on Python 3.7+ and the following main dependencies:
- `inferactively-pymdp`
- `numpy`
- `scipy`
- `pandas`
- `matplotlib`

To install the main dependency, run:
```bash
pip install inferactively-pymdp
```
Other dependencies can be installed via:
```bash
pip install numpy scipy pandas matplotlib
```

## Usage

The main workflow is demonstrated in the [tutorial notebook](tutorial/project_voodoo_tutorial.ipynb):
1. **Define Project and People**: Specify the project skill requirements and the skill profiles of DAO or lab members.
2. **Skill Matrix Construction**: The toolkit aligns individual skills to project needs, filling missing skills with zeros.
3. **Free Energy Calculation**: Computes variational free energy for each member to quantify alignment.
4. **Visualization**: Plots and ranks members by their alignment (lower free energy = better match).
5. **Squad Formation**: Selects the top-N most aligned members for the project.
6. **Partner Suggestion**: Uses KL divergence and symmetry to suggest optimal partners or sub-squads.

### Example (from the tutorial)
- See how to:
  - Define your project and people
  - Calculate and visualize alignment
  - Form the optimal squad
  - Suggest partners for collaboration

## Mathematical Details
- **Variational Free Energy**: Quantifies the surprise or misalignment between project needs and individual skills.
- **KL Divergence**: Measures the information difference between two skill distributions.
- **Symmetry**: Measures the dot product (alignment) between two skill vectors, modulated by a degree parameter.

## References
- [Active Inference and Autopoiesis](https://forum.algovera.ai/t/defining-means-to-a-web3-project-finding-synergetic-collaborators-and-funders-in-a-dao/115)
- [inferactively-pymdp documentation](https://github.com/infer-actively/pymdp)


