from readdata import read_data
from printing import print_comparison

# Column names and column indices to read
columns = {'date': 0, 'time': 1, 'tempout': 2, 'humout': 5, 'heatindex': 13}

# Data types for each column (only if non-string)
types = {'tempout': float, 'humout': float, 'heatindex': float}


# Read data from file
data = read_data(columns, types=types)


# Compute the heat index
def compute_heatindex(t, rh_pct):
   a = -42.379
   b = 2.04901523
   c = 10.14333127
   d = -0.22475541
   e = -0.00683783
   f = -0.05481717
   g = 0.00122874
   h = 0.00085282
   i = -0.00000199

   rh = rh_pct / 100

   hi = a + (b * t) + (c * rh) + (d * t * rh)
   + (e * t**2) + (f * rh**2) + (g * t**2 * rh)
   + (h * t * rh**2) + (i * t**2 * rh**2)
   return hi


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