#Purpose: Create line plot showing temperature and humidity values over time
#Name: Jordin Kolman    
#Date: 08/14/2022
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("formatdata2.csv") #baseline data is period 2)
plt.figure(); df1.Farenheit.plot(label = 'Farenheit '); df1.Humidity.plot(label = 'Humidity'); plt.legend(loc='best'); plt.suptitle('Temperature vs. Humidity')
plt.show()
