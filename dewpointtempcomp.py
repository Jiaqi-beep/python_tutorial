from mysci.readdata import read_data
from mysci.printing import print_comparison
from mysci.computation import compute_windchill

# Column names and column indices to read
columns = {'date': 0, 'time': 1, 'tempout': 2, 'windspeed': 7,
           'windchill': 12}

# Data types for each column (only if non-string)
types = {'tempout': float, 'windspeed': float, 'windchill': float}

data = read_data(columns, types=types)

# DEBUG
print(data['tempout'])


# Compute the wind chill factor
windchill = [compute_windchill(t, w) in zip(data['tempout'], data['windspeed'])]
# zip function in Python to automatically unravel the tuples


# Output comparison of data
print_comparison('WINDCHILL', data['date'], data['time'], data['windchill'], windchill)