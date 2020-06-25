import pandas as pd
import numpy as np
from sklearn import preprocessing




dataset = pd.read_csv('Python_Lesson6/Python_Lesson6_ICP/CC.csv')

#Drop missing data
dataset = dataset.select_dtypes(include=[np.number]).interpolate().dropna()


x = dataset.iloc[:,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]
y = dataset.iloc[:,-1]

print(x.shape, y.shape)


from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
scaler.fit(x)
X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array, columns = x.columns)

#KMEANS
from sklearn.cluster import KMeans
nclusters = 3 # this is the k in kmeans
km = KMeans(n_clusters=nclusters)
km.fit(X_scaled)

##SILHOUETTE SCORE
y_cluster_kmeans = km.predict(X_scaled)
from sklearn import metrics
score = metrics.silhouette_score(X_scaled, y_cluster_kmeans)
print(score)






