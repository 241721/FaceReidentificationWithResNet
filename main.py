import pickle
import functions as fun
import numpy as np

embeddings_by_id = pickle.load(open("embeddings_by_ID.pickle", "rb"))
centroids = pickle.load(open("centroids.pickle", "rb"))
distances = pickle.load(open("distances.pickle", "rb"))
distances_from_centroid = pickle.load(open("distances_from_centroid.pickle", "rb"))

#pickle.dump(distances, open("distances.pickle", "wb"))
print(fun.mean_distance_from_centroid(distances_from_centroid))
pass