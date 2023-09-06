from tslearn.metrics import dtw
from tslearn.neighbors import KNeighborsTimeSeriesClassifier
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np
from scipy.spatial import distance
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
import datetime

TRAIN_DIR = r"C:\Repos\Mgr\data_random_short\data_angles\complete\first_attempt\train.csv"
TEST_DIR = r"C:\Repos\Mgr\data_random_short\data_angles\complete\first_attempt\test.csv"

#custom metric
def DTW(a, b):   
    an = a.size
    bn = b.size
    print(datetime.datetime.now())
    print(an)
    print(bn)
    pointwise_distance = distance.cdist(a.reshape(-1,1),b.reshape(-1,1))
    cumdist = np.matrix(np.ones((an+1,bn+1)) * np.inf)
    cumdist[0,0] = 0

    for ai in range(an):
        for bi in range(bn):
            minimum_cost = np.min([cumdist[ai, bi+1],
                                   cumdist[ai+1, bi],
                                   cumdist[ai, bi]])
            cumdist[ai+1, bi+1] = pointwise_distance[ai,bi] + minimum_cost
    print(datetime.datetime.now())
    print("dupa")

    return cumdist[an, bn]

# Wczytanie danych treningowych
training_data = pd.read_csv(TRAIN_DIR, header=None)

# Podział danych treningowych na cechy (X) i etykiety klas (y)
X_train = training_data.iloc[:, 1:].values  # Pozycje markerów, bez pierwszej kolumny (etykieta klasy)
y_train = training_data.iloc[:, 0].values   # Numer klatki (etykieta klasy)

# Wczytanie danych testowych
test_data = pd.read_csv(TEST_DIR, header=None)

# Podział danych testowych na cechy (X) i etykiety klas (y)
X_test = test_data.iloc[:, 1:].values
y_test = test_data.iloc[:, 0].values

# Inicjalizacja i trening klasyfikatora k-NN
k = 5  # Liczba sąsiadów do rozważenia
parameters = {'n_neighbors':[5]}
#knn_dtw = KNeighborsTimeSeriesClassifier(n_neighbors=k, metric='dtw', verbose=1)
knn_dtw = GridSearchCV(KNeighborsClassifier(metric=DTW), parameters, verbose=1)
knn_dtw.fit(X_train, y_train)

# Klasyfikacja danych testowych
y_pred = knn_dtw.predict(X_test)
print(y_pred)

# Obliczenie dokładności klasyfikacji
accuracy = accuracy_score(y_test, y_pred)
print("Dokładność klasyfikacji: {:.2f}%".format(accuracy * 100))