# ds-bne-code-quality

This repository contains a Makefile to check and format code quality via several modules: 
- `black`: formats code by fixing spacing and adding line-breaks where code exceeds the provided line-length limit   
- `isort`: formats code by sorting imports at the beginning of .py files  
- `flake8`: checks code for styling issues, complexity, function annotations and docstrings 
- `mypy`: is a static checker. Checks whether functions are called appropriately with respect to their type definitions and any other bugs which can be detected before runtime 

## Running the code quality checker
The above modules can be run with the single make command*: 
```shell
# Runs linting and static checking on all .py source files
make check
```
*Note that you must have `make` installed to run the above command.  

## Running the code quality checker on notebook files 
The Makefile can also optionally run `nbqa` to run the above formatters, linters and static checkers on notebooks.
```shell
# Runs linting and statinc checking on all .ipynb notebook files
make check-notebook
```
### Scanning notebooks for function definitions 
All functions are encouraged to be defined in `.py` files, which are then imported and called within notebooks. 
For this reason, running `make check-notebook` will also log which notebooks cells contain function definitons and return an error until these are moved into `.py` files: 
```
python src/notebook_analyser.py notebooks
notebook_analyser: notebooks\has_functions.ipynb has function in cell number 1
notebook_analyser: notebooks\has_functions.ipynb has function in cell number 2
make: [Makefile:22: check] Error 
```
