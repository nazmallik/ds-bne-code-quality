"""Scirpt to check notebook files for function definitions."""

import argparse
import ast
import glob
import json
from pathlib import Path
from typing import List, Set


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


def get_notebook_paths(path_list:List[str])-> List[Path]:
    nb_path_list = []
    for p in path_list:
        path = Path(p)

        if path.as_posix().endswith(".ipynb"):
            nb_path_list.append(path)

        if path.is_dir():
            notebook_paths = glob.glob(
                f"{path}/**/*.ipynb", recursive=True
            )
            nb_path_list.extend([Path(nb_path) for nb_path in notebook_paths])

    return list(set(nb_path_list))


if __name__ == "__main__":
    # Initialize parser
    parser = argparse.ArgumentParser(description='Scan provided notebook files for defined functions')

    parser.add_argument(
        "nb_paths",
        nargs='+',
        type=str,
        help="Paths or directories of notebooks to analyse."
    )
    args = parser.parse_args()

    nb_paths = get_notebook_paths(args.nb_paths)
    print(nb_paths)

    contains_functions = analyze_notebooks(nb_paths)
    if contains_functions:
        exit(1)
