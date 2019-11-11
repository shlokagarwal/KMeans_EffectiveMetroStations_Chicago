import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter
import json


data = pd.read_csv('data.csv')
data = data[['Pickup Centroid Latitude','Pickup Centroid Longitude','Dropoff Centroid Latitude','Dropoff Centroid Longitude']]
data = data.dropna()
locations =[]

random_data = data.sample(100000)





X =[[0.0,0.0]]
for i,j in random_data.iterrows():
    X = np.insert(X, 0 , [j['Pickup Centroid Latitude'],j['Pickup Centroid Longitude']],axis=0)
    X = np.insert(X, 0 , [j['Dropoff Centroid Latitude'],j['Dropoff Centroid Longitude']],axis=0)    
  
X = X[:-1]

finalstring = 'var heatMapData = ['    
for i, j in random_data.iterrows():
    finalstring = finalstring + 'new google.maps.LatLng({}, {}),'.format(j['Pickup Centroid Latitude'],j['Pickup Centroid Longitude'])  
    finalstring = finalstring + 'new google.maps.LatLng({}, {}),'.format(j['Dropoff Centroid Latitude'],j['Dropoff Centroid Longitude'])      

finalstring = finalstring + '];'    
    




wcss = []
for i in range(10,40):
    print(i)
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(10, 40), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()



kmeans = KMeans(n_clusters=10, init='k-means++', max_iter=300, n_init=10, random_state=0)
pred_y = kmeans.fit_predict(X)
plt.scatter(X[:,0], X[:,1])
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
plt.show()



freq = Counter(pred_y)
  

for key, value in freq.items(): 
    print('Elements in cluster {}: {}'.format(key,value))

count_centers = sorted(freq.items())

k_centers =[]

i=0
for center in kmeans.cluster_centers_:
    k_centers.append({"lat": center[0],"long": center[1],"intensity": count_centers[i][1]/200000})
    i = i+1
    


data = {'centers': k_centers}
# To write to a file:
f = open("output.json", "w")
f.write("var json_data = ")
f.close()


with open("output.json", "a") as f:
    json.dump(data, f)

