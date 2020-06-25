import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataset = pd.read_csv('Python_Lesson6/Python_Lesson6_ICP/CC.csv')

dataset.info()

#Drop missing data
dataset = dataset.select_dtypes(include=[np.number]).interpolate().dropna()



x = dataset.iloc[:,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]
y = dataset.iloc[:,-1]

print(x.shape, y.shape)


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



##ELBOW METHOD
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11),wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()



