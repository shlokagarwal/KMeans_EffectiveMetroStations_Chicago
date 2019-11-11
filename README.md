# KMeans_EffectiveMetroStations_Chicago
I have used K-Means clustering and Chicago Taxi Data (https://www.kaggle.com/chicago/chicago-taxi-trips-bq) to find out the optimal placement of Metro stations considering there aren't any already. Add your own Google Maps API key.
The code is inside main.py and the output so obtained has been put inside heatmap.html and heatmap_with_centers.html

![Image of Sample Data](https://github.com/shlokagarwal/KMeans_EffectiveMetroStations_Chicago/blob/master/sampledata.png)


# We are using the Pickup and Dropoff Latitude and longitude to get an idea of the density of transportation requirement.

The heatmap which came up with just 200000 latitude,longitude pairs
Here, we can see that its practical because there is some density near the Chicago Airport.

![Image of Heat Map](https://github.com/shlokagarwal/KMeans_EffectiveMetroStations_Chicago/blob/master/heatmap.png)

# Now we will use K-means clustering WCSS graph to find out the optimal number of clusters.

![Image of Heat Map](https://github.com/shlokagarwal/KMeans_EffectiveMetroStations_Chicago/blob/master/wcss.png)

As we can see here, there is no such elbow point and the wcss value keeps on decreasing. This is probably because Chicago is a very big city and will require much more metro stations than 40.(fact: it has 145 metro stations under Chicago "L")

# If we consider k=10 (10 metro stations), the positions of them found are shown below
![Image of Heat Map with centers](https://github.com/shlokagarwal/KMeans_EffectiveMetroStations_Chicago/blob/master/10_clusters.png)

# How to change the api key.
Scroll down on the html files and change the following.
![Image of Heat Map](https://github.com/shlokagarwal/KMeans_EffectiveMetroStations_Chicago/blob/master/apikey.png)

Do check out the ppt.
https://github.com/shlokagarwal/KMeans_EffectiveMetroStations_Chicago/blob/master/how%20can%20we%20effectively%20build%20metro%20stations%3F.pptx
