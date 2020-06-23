import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

houseDF = pd.read_csv('Python_Lesson5/train.csv')

# PLOT WITH ANOMOLIES
x = houseDF.SalePrice
y = houseDF.GarageArea
plt.scatter(x, y, marker='o')
plt.xlabel('Sale Price')
plt.ylabel('Garage Area')
plt.show()

# NEW PLOT WITHOUT ANOMALIES
houseDF = houseDF[houseDF['SalePrice'] < 600000]
houseDF = houseDF[houseDF['GarageArea'] < 1200]
houseDF = houseDF[houseDF['GarageArea'] > 0]
x = houseDF.SalePrice
y = houseDF.GarageArea

plt.scatter(x, y, marker='o')
plt.xlabel('Sale Price')
plt.ylabel('Garage Area')
plt.show()



