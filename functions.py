import numpy as np
import progressbar as pb

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
    pass

# min and max between classes
def fun1():
    pass

# średnia odleglość między klasami
def fun2():
    pass

# średnia odleglość od centroidu wewnątrz klasy
def fun3():
    pass

# najbardziej oddalone zdjęcia wewnątrz klasy
def fun4():
    pass

#najmniej oddalone zdjęcia między klasami
def fun5():
    pass



