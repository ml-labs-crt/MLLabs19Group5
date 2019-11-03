import numpy as np

from sklearn.cluster import KMeans
from sklearn.manifold import TSNE


def gen_fake_vectors():
    """ Generate random data withe expected shapes of our real data """
    
    return [[np.random.randint(1, 100) for i in range(96)] for j in range(102)]


def fit_hardKMeans(X, neighbours):
    """ Fit KMeans to X with the given number of neighbours """
    
    model = KMeans(neighbours)
    model.fit(X)
    return model


def genTSNE(X, dimensions):
    """ Embed X in a lower dimensional space for graphics """
    
    embedding = TSNE(dimensions).fit_transform(X)
    return embedding
