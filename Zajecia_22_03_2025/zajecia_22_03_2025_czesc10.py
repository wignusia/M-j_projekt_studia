##krotka1=(57,7,24,22,97,56)
#krotka2=krotka1[2:5]
#print(krotka2)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs

# Generowanie przykładowych danych - 2D
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Stosowanie algorytmu DBSCAN
dbscan = DBSCAN(eps=0.3, min_samples=10)
y_dbscan = dbscan.fit_predict(X)

# Wizualizacja wyników
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y_dbscan, cmap='viridis')
plt.title('Klasteryzacja z użyciem DBSCAN')
plt.xlabel('Cecha 1')
plt.ylabel('Cecha 2')
plt.colorbar(label='Identyfikator klastra')
plt.show()
