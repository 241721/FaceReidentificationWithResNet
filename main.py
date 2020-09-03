import pickle
import functions as fun
import numpy as np

embeddings_by_id = pickle.load(open("embeddings_by_ID.pickle", "rb"))
centroids = pickle.load(open("centroids.pickle", "rb"))
distances = pickle.load(open("distances.pickle", "rb"))

#distances = fun.distances_between_classes(centroids)
#pickle.dump(distances, open("distances.pickle", "wb"))
fun.fun1(distances)
pass