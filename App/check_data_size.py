import pandas as pd

# Ścieżki do zbiorów danych
TRAIN_DIR1 = r"C:\Repos\Mgr\data_random\data_powers\complete\first_attempt\train.csv"
TRAIN_DIR2 = r"C:\Repos\Mgr\data_random_short\data_powers\complete\first_attempt\train.csv"
TRAIN_DIR3 = r"C:\Repos\Mgr\data_random_long\data_powers\complete\first_attempt\train.csv"

# Wczytanie danych treningowych
training_data1 = pd.read_csv(TRAIN_DIR1, header=None)
training_data2 = pd.read_csv(TRAIN_DIR2, header=None)
training_data3 = pd.read_csv(TRAIN_DIR3, header=None)

print("===== 100 =====")
print(training_data1.info())
print("===== 10 =====")
print(training_data2.info())
print("===== 250 =====")
print(training_data3.info())