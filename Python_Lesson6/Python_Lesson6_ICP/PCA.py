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
# Fit on training set only.
scaler.fit(x)

x_scaler = scaler.transform(x)
pca = PCA(2)
x_pca = pca.fit_transform(x_scaler)

df2 = pd.DataFrame(data=x_pca)
finaldf = pd.concat([df2,dataset[['TENURE']]],axis=1)
print(finaldf)

x = finaldf.iloc[:,[0,1,2]]
y = finaldf.iloc[:,-1]

print(x.shape, y.shape)



from sklearn.cluster import KMeans
nclusters = 7 # this is the k in kmeans
km = KMeans(n_clusters=nclusters)
km.fit(x)

#predict the cluster for each data point
y_cluster_kmeans = km.predict(x)
from sklearn import metrics
score = metrics.silhouette_score(x, y_cluster_kmeans)
print(score)



##elbow method to know the number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1,16):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,16),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

