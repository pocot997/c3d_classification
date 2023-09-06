import pandas as pd

TRAIN_PATH = r"C:\Repos\Mgr\data_random_long\data_modeled_markers\complete"
TEST_PATH = r"C:\Repos\Mgr\data_random_long\data_modeled_markers\complete"

TRAIN_NAME = r"\train.csv"
TEST_NAME = r"\test.csv"

attempts = [r"\first_attempt", r"\second_attempt", r"\third_attempt"]

def replace_non_convertible_values(data):
    counter = 0
    for column in data.columns:
        for idx, value in enumerate(data[column]):
            try:
                # Próba przekonwertowania wartości na float
                float_value = float(value)
            except ValueError:
                # Zastąpienie wartości, które nie mogą być przekonwertowane na float'a, wartością 0
                data.at[idx, column] = 0
                counter = counter + 1
    print(f"Poprawiono {counter} komórek")

def fix_file(file_path):
    # Wczytanie pliku CSV
    data = pd.read_csv(file_path, header=None)

    # Znalezienie wierszy, które zawierają wartość NaN
    nan_rows = data[data.isnull().any(axis=1)]

    counter = 0
   # Wypisanie pierwszej komórki dla wierszy z wartościami NaN
    for idx in nan_rows.index:
        counter = counter + 1

    #print(f"Usunięto {counter} wierszy")
    print(f"Poprawiono {counter} wierszy")

    # Usunięcie tych wierszy
    #data = data.dropna()

    # Zamiana wszystkich wartości NaN na 0
    data = data.fillna(0)

    replace_non_convertible_values(data)

    # Zapisanie zmodyfikowanych danych do pliku CSV
    data.to_csv(file_path, header=False, index=False)

for attempt in attempts:
    train_path = TRAIN_PATH + attempt + TRAIN_NAME
    test_path = TEST_PATH + attempt + TEST_NAME

    fix_file(train_path)
    fix_file(test_path)
    print("--------------------------")

