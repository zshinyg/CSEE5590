import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error




WineQualityDF = pd.read_csv('Python_Lesson5/winequality-red.csv')


#Drop missing data
data = WineQualityDF.select_dtypes(include=[np.number]).interpolate().dropna()

#Check Data
print(WineQualityDF.quality.describe())

#Check for Skewness -- Skewness is approximately symmetric
print ("Skew is:", WineQualityDF.quality.skew())
#plt.hist(WineQualityDF.quality, color='blue')
#plt.show()

#Correlation -- alchohol, volatile acidity, and sulphates are the 3 highest correlated features
numeric_features = WineQualityDF.select_dtypes(include=[np.number])
corr = numeric_features.corr()
print(corr['quality'],'\n') 

#Build Linear Model
y = WineQualityDF.quality
X = data[['alcohol','volatile acidity', 'sulphates']]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33)
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)

#R2 Score
print ("R^2 is: \n", model.score(X_test, y_test))

#RMSE
predictions = model.predict(X_test)
print ('RMSE is: \n', mean_squared_error(y_test, predictions))

##visualize

actual_values = y_test
plt.scatter(predictions, actual_values, alpha=0.25, color='b') #alpha helps to show overlapping data
plt.xlabel('Predicted Quality')
plt.ylabel('Actual Quality')
plt.title('Linear Regression Model')
plt.show()


