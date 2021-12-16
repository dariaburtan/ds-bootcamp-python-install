# Test that statsmodels works correctly

try:
  from statsmodels.tsa.api import ExponentialSmoothing
  print("Success!")
except:
  print("Failed to load ExponentialSmoothing")
