"""Scirpt to check notebook files for function definitions."""

import argparse
import ast
import glob
import json
from typing import List


def has_function(code: str) -> bool:
    """Checks whether provided source code has a function in it.

    Args:
        code (str): The source code as a strig

    Returns:
        bool: True if source code contains a function and False otherwise
    """
    tree = ast.parse(code)
    for node in ast.walk(tree):
        # print(node)
        if isinstance(node, ast.FunctionDef):
            return True
    return False


def analyze_notebooks(notebook_paths: List[str]) -> bool:
    """Iterates over provided notebook paths and checks whether any notebook code cells contain function definitions.

    Args:
        notebook_paths (List[str]): A list of notebook file paths

    Returns:
        bool: True if any of the notebooks have a function in them and False otherwise
    """
    raise_error = False
    for notebook in notebook_paths:
        with open(notebook, "r") as notebook_file:
            notebook_contents = json.load(notebook_file)

            has_function_flag = False
            for cell_id, cell in enumerate(notebook_contents["cells"]):
                if cell["cell_type"] == "code":
                    source_code = "".join(cell["source"])
                    if has_function(source_code):
                        print(
                            f"notebook_analyser: {notebook} has function in cell number {cell_id}"
                        )
                        has_function_flag = True
                        raise_error = True

            if not has_function_flag:
                print(
                    f"notebook_analyser: {notebook} has no functions in it :)"
                )

    return raise_error


if __name__ == "__main__":
    # Initialize parser
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-n",
        "--nb-directory",
        help="Source directory of notebooks to analyze.",
        required=True,
    )
    args = parser.parse_args()

    notebook_paths = glob.glob(
        f"{args.nb_directory}/**/*.ipynb", recursive=True
    )

    contains_functions = analyze_notebooks(notebook_paths)
    if contains_functions:
        exit(1)
