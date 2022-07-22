'''
#example of how to import data from NOAA

from noaa_sdk import NOAA

n = NOAA()

res = n.get_forecasts('76549', 'US', 'forecastGridData')

for i in res:
    print(i)
'''

#Purpose: Build weather database from NOAA data
#Name: Jordin Kolman
#Date: 07/22/2022
#