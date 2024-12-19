"""
Main
Owners: 

_____/\\\\\\\\\\\____/\\\\\\\\\\\\__________/\\\\\_______/\\\\\\\\\\\\\\\_        
 ___/\\\/////////\\\_\/\\\////////\\\______/\\\///\\\____\/\\\///////////__       
  __\//\\\______\///__\/\\\______\//\\\___/\\\/__\///\\\__\/\\\_____________      
   ___\////\\\_________\/\\\_______\/\\\__/\\\______\//\\\_\/\\\\\\\\\\\_____     
    ______\////\\\______\/\\\_______\/\\\_\/\\\_______\/\\\_\/\\\///////______    
     _________\////\\\___\/\\\_______\/\\\_\//\\\______/\\\__\/\\\_____________   
      __/\\\______\//\\\__\/\\\_______/\\\___\///\\\__/\\\____\/\\\_____________  
       _\///\\\\\\\\\\\/___\/\\\\\\\\\\\\/______\///\\\\\/_____\/\\\_____________ 
        ___\///////////_____\////////////__________\/////_______\///______________
"""

import numpy as np
import pandas as pd

import constants as c
from scripts import (
    aero,
    axial,
    bending,
    dynamic,
    recovery,
    shear,
)

from utils import (
    input_handler,
    output_handler,
)


def main():

    # Example Input Handler
    file_path = "data/inputs/SDOF_inputs.xlsx"  # Path to the input file
    inputs = pd.read_excel(file_path)  # Read the input file into a Pandas DataFrame

    # a try-except block is used to catch the KeyError exception that is raised when the parameter is not found in the DataFrame
    try:
        parmeter_1 = input_handler.get_parameter(
            inputs, "Parameter 1 [units]"
        )  # Get the value of the parameter from the DataFrame
        parmeter_2 = input_handler.get_parameter(
            inputs, "Parameter 2 [units]"
        )  # Get the value of the parameter from the DataFrame
    except KeyError as e:
        print(e)  # Print the error message

    print(parmeter_1)
    print(parmeter_2)

    # Example Dictionaries
    # A dictionary is a collection of key-value pairs. Each key-value pair maps the key to its corresponding value.

    tanks = {  # A dictionary containing key-value pairs
        "mass": 10,  # A key-value pair
        "length": 13,
        "diameter": 0.1,
        "cd": 0.5,
        "material": "aluminum",
    }
    lower_airframe = {
        "mass": 30,
        "length": 10,
        "diameter": 0.1,
        "material": "aluminum",
    }

    rocket = {  # A dictionary containing dictionaries of key-value pairs
        "lower airframe": lower_airframe,
        "tanks": tanks,
    }

    # Accessing specific values from the dictionaries
    print(rocket["lower airframe"]["mass"])


if __name__ == "__main__":
    main()
