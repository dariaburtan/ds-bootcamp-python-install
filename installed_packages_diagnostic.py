# Script for testing whether packages/modules are installed.

# Author: Tom Fowler
# Version: 0.0.0.9000
# Last Update: 2021-12-15

# Imports
import sys
import importlib.util as imputil

# List of packages to test presence for
packages = ["math", "numpy", "pandas", "matplotlib", "seaborn", "scipy",
            "sklearn", "statsmodels", "nltk", "TextBlob", "bs4",
            "requests", "datetime", "random"]

# Define function
def test_installed(pkg):
    
    if pkg in sys.modules:
        print(f'Python module \'{pkg}\' is already installed in sys.modules\n')
        out = True
    elif imputil.find_spec(pkg) != None:
        print(f'A library matching the name \'{pkg}\' is available for import\n')
        out = True
    else:
        print(f'Could not find {pkg} in sys.modules or with implib.find_spec()\n')
        out = False
    return out

installed = list(zip(packages, [test_installed(pkg) for pkg in packages]))
