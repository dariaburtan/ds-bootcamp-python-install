# Script for testing whether packages/modules are installed.

# Author: Tom Fowler
# Version: 0.0.0.9001
# Last Update: 2021-12-15

# Imports
import sys
import importlib.util as imputil

# List of packages to test presence for
packages = ["math", "numpy", "pandas", "matplotlib", "seaborn", "scipy",
            "sklearn", "statsmodels", "nltk", "textblob", "bs4",
            "requests", "datetime", "random", "jupyter", "jupyterlab",
            "IPython"]

# Define function
def test_installed(pkg):

    if pkg in sys.modules:
        print(f'\'{pkg}\' found in sys.modules\n')
        out = True
    elif imputil.find_spec(pkg) != None:
        print(f'\'{pkg}\' found with find_spec()\n')
        out = True
    else:
        print(f'**Missing pkg**: \'{pkg}\' not in sys.modules or found with implib.find_spec()\n')
        out = False
    return out

installed = list(zip(packages, [test_installed(pkg) for pkg in packages]))
