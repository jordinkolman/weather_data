#Purpose: Create a histogram of humidity data from the second period
#Name: Jordin Kolman
#Date: 8/14/2022
import pandas as pd
import matplotlib.pyplot as plt
df2 = pd.read_csv("formatdata2.csv")
df2['Humidity'].hist(bins=10, alpha=0.5); plt.suptitle('Histogram of Humidity')
plt.show()
