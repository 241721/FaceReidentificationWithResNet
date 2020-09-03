import numpy as np
import progressbar as pb
import math

# dzieli tablicę z embeddingami na tożsamości (embeddings) - baza utworzona za pomocą encode_faces.py
def divide_by_id(embeddings):
    id_amount = 10177
    embeddings_by_id = [[] for x in range(id_amount)]
    i = 0
    for embedding in embeddings['names']:
        embeddings_by_id[int(embedding)-1].append(embeddings['encodings'][i])
        i += 1
    return embeddings_by_id


# tworzy centroidy z tożsamości (embeddings_by_ID - baza embeddingów podzielona na tożsamości)
# najlepiej funkcją divide_by_id
def make_centroids(embeddings_by_id):
    centroids = []
    for i in range(len(embeddings_by_id)):
        sum = 0
        for embedd in embeddings_by_id[i]:
            sum += embedd
        if len(embeddings_by_id[i]) == 0:
            centroids.append(0)
        else:
            centroids.append(sum/len(embeddings_by_id[i]))
    return centroids


# tworzy listy odleglości między daną klasą a innymi klasami z centroidów
def distances_between_classes(centroids):
    test_range = 2293 # dla testów DO USUNIĘCIA PÓŹNIEJ
    distances = [[] for x in range(test_range)] # dla testów DO USUNIĘCIA PÓŹNIEJ
    j = 0
    for centroid in pb.progressbar(centroids):
        for i in range(test_range): # dla testów DO USUNIĘCIA PÓŹNIEJ
            # jeśl
            if type(centroid) != np.ndarray or type(centroids[i]) != np.ndarray:
                distances[j].append(np.nan)
            else:
                dist = np.linalg.norm(centroid - centroids[i])
                distances[j].append(dist)
        j += 1
        if j == test_range: # dla testów DO USUNIĘCIA PÓŹNIEJ
            break
    return distances


# min and max between classes DO DOKONCZENIA!!!
def fun1(distances):
    mini = 10
    maxi = 0
    for i in pb.progressbar(range(len(distances)-1)):
        for j in range(i, len(distances)):
            dist = list(filter(lambda a: a > 0.0, distances[j]))
            dist = [number for number in dist if not math.isnan(number)]
            if len(dist) == 0:
                continue
            m = min(dist)

            if m < mini:
                mini = m
                for x in range(len(distances[j])):
                    if distances[j][x] == mini:
                        print("min: " + str(mini) + " between classes " + str(x+1) + " and " + str(j+1))

            else:
                ma = max(dist)
                if ma > maxi:
                    maxi = ma
                    for x in range(len(distances[j])):
                        if distances[j][x] == maxi:
                            print("max: " + str(maxi) + " between classes " + str(x+1) + " and " + str(j+1))


# średnia odleglość między klasami -- CelebA: 0.7080265435031082
def mean_dist_between_classes(distances):
    sum = 0
    i = 0
    for dist in distances:
        d = list(filter(lambda a: a > 0.0, dist))
        m = np.mean(d)
        if math.isnan(m):
            continue
        else:
            sum += m
            i += 1
    return sum/i


# odleglości od centroidu wewnątrz klasy
def fun3(embeddings_by_id, centroids):
    pass

# średnia odleglość od centroidu wewnątrz klasy
def fun3b():
    pass

# najbardziej oddalone zdjęcia wewnątrz klasy
def fun4():
    pass

#najmniej oddalone zdjęcia między klasami
def fun5():
    pass


