import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt




dataset = pd.read_csv('Python_Lesson6/Python_Lesson6_ICP/CC.csv')

#Drop missing data
dataset = dataset.select_dtypes(include=[np.number]).interpolate().dropna()


x = dataset.iloc[:,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]
y = dataset.iloc[:,-1]

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x)

x_scaler = scaler.transform(x)
pca = PCA(2)
x_pca = pca.fit_transform(x_scaler)

pca_datset = pd.DataFrame(data=x_pca)
finaldf = pd.concat([pca_datset,dataset[['TENURE']]],axis=1)
print(finaldf)

x = finaldf.iloc[:,[0,1,2]]
y = finaldf.iloc[:,-1]

##KMEANS
from sklearn.cluster import KMeans
nclusters = 3 # this is the k in kmeans
km = KMeans(n_clusters=nclusters)
km.fit(x)

##SILHOUETTE SCORE
y_cluster_kmeans = km.predict(x)
from sklearn import metrics
score = metrics.silhouette_score(x, y_cluster_kmeans)
print(score)


