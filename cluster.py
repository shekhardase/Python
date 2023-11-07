from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([3, 1, 12, 1, 6, 6, 5, 6, 7, 8, 9, 8, 9, 9, 8])
x2 = np.array([5, 4, 5, 6, 5, 8, 6, 7, 1, 2, 1, 2, 3, 2, 3])
plt.show()
plt.xlim([0,10])
plt.ylim([0,10])
plt.title('Database')
plt.scatter(x1 , x2)
plt.show()

plt.plot()

x = np.array[(list (zip(x1, x2)))].reshape(len(x1),2)

color = ['b','g' , 'r']
marker = ['o' , 'v','s']
distortions = []
k  = range(1,10) 

for k in k :
    kmeanModel = KMeans(n_cluster = k).fit(x)
    kmeanModel.fit(x)
    distortions.append(sum(np.min(cdist(x,kmeanModel.cluster_centers,'euclidean'),axis=1))/x.shape[0])

#plot elbow
plt.plot(k,distortions,'bx_')
plt.xlabel('k')
plt.ylabel('distortions')
plt.title('The elbow method to get optimal value of k')
plt.show()


