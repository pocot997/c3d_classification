import pandas as pd
import datetime as dt
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.svm import SVC

# Ścieżki do zbiorów danych
TRAIN_DIR = r"C:\Repos\Mgr\data_normal\data_markers\complete"
TEST_DIR = r"C:\Repos\Mgr\data_normal\data_markers\complete"

TRAIN_NAME = r"\train.csv"
TEST_NAME = r"\test.csv"

attempts = [r"\first_attempt", r"\second_attempt", r"\third_attempt"]

# Parametry danych
#data_labels = [406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 433, 434, 435, 442, 445, 446, 448, 449, 451, 453, 455, 456]
data_labels = [406, 407, 409, 410, 411, 412, 414, 415, 416, 417, 418, 419, 433, 434, 435, 442, 445, 446, 448, 449, 451, 453, 455, 456]

counter = 0

for attempt in attempts:

    train_file = TRAIN_DIR + attempt + TRAIN_NAME
    test_file = TEST_DIR + attempt + TEST_NAME

    # Wczytanie danych treningowych
    training_data = pd.read_csv(train_file, header=None)

    # Podział danych treningowych na cechy (X) i etykiety (y)
    X_train = training_data.iloc[:, 1:].values
    y_train = training_data.iloc[:, 0].values

    # Wczytanie danych testowych
    test_data = pd.read_csv(test_file, header=None)

    # Podział danych testowych na cechy (X) i etykiety (y)
    X_test = test_data.iloc[:, 1:].values
    y_test = test_data.iloc[:, 0].values

    # Dodatkowe parametry modelu

    # Inicjalizacja i trening klasyfikatora
    model = SVC(probability=True)
    start_time = dt.datetime.now()
    model.fit(X_train, y_train)

    # Klasyfikacja danych testowych
    y_pred = model.predict(X_test)
    end_time = dt.datetime.now()
    fit_time = end_time - start_time

    # Obliczenie dokładności klasyfikacji
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average = "weighted")
    recall = recall_score(y_test, y_pred, average = "weighted")
    f1 = f1_score(y_test, y_pred, average = "weighted")

    # Obliczenie wartości ROC AUC dla każdej z klas
    roc_auc_scores = []
    for i in range(len(data_labels)):
        y_true = [1 if x == data_labels[i] else 0 for x in y_test]
        y_pred = model.predict_proba(X_test)[:, i]
        roc_auc_scores.append(roc_auc_score(y_true, y_pred))

    # Obliczenie średniej wartości ROC AUC
    multi_class_roc_auc = sum(roc_auc_scores) / len(roc_auc_scores)

    content = "{} \t {:.4f} \t {:.4f} \t {:.4f}  \t {:.4f}  \t {:.4f}  \t {:.4f}".format(fit_time, accuracy, 1 - accuracy, precision, recall, f1, multi_class_roc_auc)
    
    if(counter == 0):
        with open(TRAIN_DIR + r"\svm.txt", 'w') as file:
            file.write(content + '\n')
    else:
        with open(TRAIN_DIR + r"\svm.txt", 'a') as file:
            file.write(content + '\n')

    counter = counter + 1

    # Wizualizacja wyników klasyfikacji
    print(fit_time)
    print("Accuracy: {:.4f}".format(accuracy))
    print("Error rate: {:.4f}".format(1 - accuracy))
    print("Precision: {:.4f}".format(precision))
    print("Recall: {:.4f}".format(recall))
    print("F1: {:.4f}".format(f1))
    print("Roc Auc: {:.4f}".format(multi_class_roc_auc))
    #print(y_pred)
    print("-------------------------------------------")
