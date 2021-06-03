from readdata import read_data
from printing import print_comparison
from computation import compute_heatindex

# Column names and column indices to read
columns = {'date': 0, 'time': 1, 'tempout': 2, 'humout': 5, 'heatindex': 13}

# Data types for each column (only if non-string)
types = {'tempout': float, 'humout': float, 'heatindex': float}


# Read data from file
data = read_data(columns, types=types)


# Compute the wind chill factor
# windchill = []
# 	# zip function in Python to automatically unravel the tuples
# for temp, windspeed in zip(data['tempout'], data['windspeed']):
#    windchill.append(compute_windchill(temp, windspeed))


# # Output comparison of data
# print('                ORIGINAL  COMPUTED')
# print(' DATE    TIME  WINDCHILL WINDCHILL DIFFERENCE')
# print('------- ------ --------- --------- ----------')
# zip_data = zip(data['date'], data['time'], data['windchill'], windchill)
# for date, time, wc_orig, wc_comp in zip_data:
#    wc_diff = wc_orig - wc_comp
#    print(f'{date} {time:>6} {wc_orig:9.6f} {wc_comp:9.6f} {wc_diff:10.6f}')

# >6 right justified and take up 6 spaces
# 9.6f fill 9 spaces with 6 of them being after the decimal point

heatindex = []

for temp, hum in zip(data['tempout'], data['humout']):
   heatindex.append(compute_heatindex(temp, hum))


# Output comparison of data
print_comparison('HEAT INDX', data['date'], data['time'], data['heatindex'], heatindex)