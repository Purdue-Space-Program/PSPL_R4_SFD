# Rocket 4 SFOF

This repository contains Structures Determenation Of Forces (SDOF). This is work in progress and is subject to change.

The SDOF model uses the vehicle's geometry, mass properties, and flight conditions to compute compressive forces, shear forces, bending moments, and torsion at specific cross-sections of the rocket.

## Filesystem Hierarchy

```plaintext
.
└── PSPL_R4_SDOF/
    ├── data/
    │   ├── inputs/
    │   │   └── SFOF_inputs.xlsx
    │   └── outputs/
    │       └── YYYY-MM-DD_HH-MM-SS/
    │           ├── charts/
    │           ├── SDOF_outputs.xlsx
    │           └── SDOF_inputs.xlsx
    ├── scripts/
    │   ├── aero.py
    │   ├── axial.py
    │   ├── shear.py
    │   ├── bending.py
    │   ├── dynamic.py
    │   └── recovery.py
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
