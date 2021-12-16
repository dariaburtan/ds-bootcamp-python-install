# ds-bootcamp-python-install
Teaching resources for installing Python with Anaconda

# Package Installation

## Easy install packages
Run this in your Anacona (base) environment

```
conda install numpy pandas matplotlib seaborn scipy scikit-learn statsmodels nltk
```

## Notebooks: jupyter, jupyterlab
Run this in your Anacona (base) environment

```
conda install -c conda-forge jupyter jupyterlab
```

## TextBlob

Run this in your Anacona (base) environment

```
conda install -c conda-forge textblob
```

# Check your installed packages with Powershell (Windows)

## Search all
```
conda list
```

## Search for packages with a matching name

### Syntax:

```
conda list | findstr <string>
```

### Example:

For example, search for everything matching 'jup' (e.g. 'jupyter')

```
conda list | findstr jup
```

# Check your installed packages with UNIX terminal (macOS, Linux)

## Search all
```
conda list
```

## Search for packages with a matching name

### Syntax:

```
conda list | grep <string>
```

### Example:

For example, search for everything matching 'jup' (e.g. 'jupyter')

```
conda list | grep jup
```
