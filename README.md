# ds-bootcamp-python-install
Teaching resources for installing Python with Anaconda

# Package Installation

## Easy install packages
Run this in your Anaconda (base) environment

```
conda install numpy pandas matplotlib seaborn scipy scikit-learn statsmodels nltk
```

## Notebooks: jupyter, jupyterlab
Run this in your Anaconda (base) environment

```
conda install -c conda-forge jupyter jupyterlab
```

## TextBlob

Run this in your Anaconda (base) environment

```
conda install -c conda-forge textblob
```

# Get a list of ALL your installed packages

```
conda list
```

# Get a list of your installed packages with names that match a string

## Windows Powershell

### Syntax:

```
conda list | findstr <string>
```

### Example:

For example, search for everything matching 'jup' (e.g. 'jupyter')

```
conda list | findstr jup
```

## UNIX terminal (macOS, Linux)

### Syntax:

```
conda list | grep <string>
```

### Example:

For example, search for everything matching 'jup' (e.g. 'jupyter')

```
conda list | grep jup
```
