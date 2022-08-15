#Purpose: Create box plot for period 2 data
#Name: Jordin Kolman
#Date: 08/14/2022
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("formatdata.csv")
df1.boxplot(); plt.suptitle('Period 1 box plot')
plt.show()
