import ast
import glob


def has_function(code):
    tree = ast.parse(code)
    for node in ast.walk(tree):
        print(node)
        node.
        if isinstance(node, ast.FunctionDef):
            return True
    return False


# Example usage:
source_code = """
def my_function():
    print("Hello, world!")
"""


notebooks = glob.glob("notebooks/**/*.ipynb", recursive=True)

for n in notebooks[:1]:
    with open(n) as notebook_file:
        notebook_text = notebook_file.read()
        print(notebook_text)
        if has_function(notebook_text):
            print(f"{n}")

# if has_function(source_code2):
#     print("The source code contains at least one function.")
# else:
#     print("The source code does not contain any functions.")
