""" Module with functions to apply the black formatter."""

import os


def gen_python_input(python_code: str, file_name: str) -> None:
    """Generates a python file from a given string."""

    # Writes the code into a file
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(python_code)


def gen_python_black_formatter_output(file_name: str) -> None:
    """Applies the black formatter to a python file"""

    # Define the os command to execute black formatter
    cmd = f"python -m black {file_name} -v"

    # Executes the command
    os.system(cmd)


def get_formatted_string(file_name: str) -> str:
    """Returns the string of the python code.
    Receives a file name to read.
    """

    # Reads the file
    with open(file_name, "r", encoding="utf-8") as f:
        python_code = f.read()

    return python_code


def remove_temp_file(file_name: str) -> None:
    """Delete the temporal file"""

    # Define the os command to delete the temporal file
    cmd = f"rm {file_name}"

    # Executes the command
    os.system(cmd)


def black_formatter_converter(input_python_code: str) -> str:
    """Returns a string with the black formatter applied.
    Receives a python code, create a python file,
    applies the black formatter and then get string from it.
    """

    # Temporal file name to be used as input
    temp_file_name = "temp_file.py"

    # Creating the input python file
    gen_python_input(input_python_code, temp_file_name)

    # Aplying the black formatter
    gen_python_black_formatter_output(temp_file_name)

    # Getting the code from the formatted file
    output_python_code = get_formatted_string(temp_file_name)

    # Removing the temporal file
    remove_temp_file(temp_file_name)

    return output_python_code
