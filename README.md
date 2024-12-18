# Rocket 4 SFOG

This repository contains Structures Determenation Of Forces (SDOF). This is work in progress and is subject to change.

The SDOF model uses the vehicle's geometry, mass properties, and flight conditions to compute compressive forces, shear forces, bending moments, and torsion at specific cross-sections of the rocket.

## Filesystem Hierarchy

```plaintext
└── PSPL_ROCKET_4_SDOF/
    ├── data/
    │   ├── inputs/
    │   │   └── rocket_defining_inputs.xlsx
    │   └── outputs/
    │       └── YYYY-MM-DD_HH-MM-SS/
    │           ├── possible_rockets.xlsx
    |           └── rocket_defining_inputs.xlsx
    ├── scripts/
    │   ├── combustion.py
    │   ├── propulsion.py
    │   ├── structural.py
    │   ├── fluids.py
    │   └── trajectory.py
    ├── tests/
    │   ├── test_combustion.py
    │   ├── test_propulsion.py
    │   ├── test_structural.py
    │   ├── test_fluids.py
    │   └── test_trajectory.py
    ├── utils/
    │   ├── clean_up.py
    │   └── rocket_defining_input_handler.py
    ├── main.py
    ├── .gitignore
    ├── README.md
    └── requirements.txt

```

## Installation

1. Clone the repository

```bash
git clone https://github.com/Purdue-Space-Program/PSPL_Rocket_4_SDOF.git
```

2. Navigate to the repository

```bash
cd PSPL_Rocket_4_SDOF
```

3. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate
```

4. Install the required packages

```bash
pip3 install -r requirements.txt
```

## Usage

1. Edit the `SDOF_inputs.xlsx` file in the `data/inputs/` directory to define the key parameters.
2. Run the main script

```bash
python3 main.py
```

## Additional Information

- **Data**: Input data should be placed in `data/inputs/`. Output data will be generated in `data/outputs/`.
- **Scripts**: Contains the core logic for different components of the sizing script.
