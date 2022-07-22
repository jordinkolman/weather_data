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
# See https://pypi.org/project/noaa-sdk/ for details on noaa-sdk package used

from noaa_sdk import noaa
import sqlite3
import datetime

# parameters for retrieving NOAA weather data
zipCode = "76549"
country = "US"
# date-time format is yyyy-mm-ddThh:mm:ssZ - times are Zulu time (GMT)

# gets most recent 14 days of data
today = datetime.datetime.now()
past = today - datetime.timedelta(days=14)
startDate = past.strftime("%Y-%m-%dT00:00:00Z")
endDate = today.strftime("%Y-%m-%dT23:59:59Z")

# create connection - this creates database if one doesn't already exist
print("Preparing database...")
dbFile = "weather.db"
conn = sqlite3.connect(dbFile)
# create cursor to execute SQL commands
cur = conn.cursor()

# drop previous version of table, if any, so we start fresh each time
dropTableCmd = "DROP TABLE IF EXISTS observations;"
cur.execute(dropTableCmd)

# create new table to store observations
createTableCmd = """CREATE TABLE IF NOT EXISTS OBSERVATIONS (
            timestamp TEXT NOT NULL PRIMARY KEY,
            windspeed REAL,
            temperature REAL,
            relativeHumidity REAL,
            windDirection INTEGER,
            barometricPressure INTEGER,
            visibility INTEGER,
            textDescription TEXT
            );"""
cur.execute(createTableCmd)
print("Database prepared")

# get hourly observations from NOAA Weather Service API
print("Getting weather data... ")
n = noaa.NOAA()
observations = n.get_observations(zipCode, country, startDate, endDate)

#populate table with weather observations
print("Inserting rows... ")
insertCmd = """INSERT INTO observations
            (timestamp, windSpeed, temperature, relativeHumidity, windDirection, barometricPressure, visibility, textDescription) 
        VALUES
            (?, ?, ?, ?, ?, ?, ?, ?)"""
count = 0
for obs in observations:
    insertValues = (obs["timestamp"],
                obs["windSpeed"]["value"],
                obs["temperature"]["value"],
                obs["relativeHumidity"]["value"],
                obs["windDirection"]["value"],
                obs["barometricPressure"]["value"],
                obs["visibility"]["value"],
                obs["textDescription"],)
    cur.execute(insertCmd, insertValues)
    count += 1
    if count > 0:
        cur.execute("COMMIT;")
    print(count, "rows inserted")
print("Database load complete!")

