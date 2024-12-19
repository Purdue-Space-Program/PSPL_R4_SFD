def get_parameter(df, parameter_name):
    """
    Search for the parameter in the DataFrame and return its value.

    Args:
    df (DataFrame): The DataFrame containing the variables and their values.
    parameter_name (str): The name of the parameter to search for.

    Returns:
    Value of the parameter if found, else None.
    """
    if parameter_name in df.columns:
        return df[parameter_name].iloc[0]
    else:
        raise KeyError(f"Parameter '{parameter_name}' not found in the Excel file.")
