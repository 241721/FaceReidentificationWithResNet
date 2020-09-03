import pickle
import functions as fun


embeddings_by_id = pickle.load(open("embeddings_by_ID.pickle", "rb"))
centroids = pickle.load(open("centroids.pickle", "rb"))
distances = fun.distances_between_classes(centroids)
#distances = pickle.load(open("distances.pickle", "rb"))
#pickle.dump(distances, open("distances.pickle", "wb"))
pass