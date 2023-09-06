import glob
import csv

TRAIN_PATH = r"C:\Repos\Mgr\data_random_long\data_modeled_markers\train"
TEST_PATH = r"C:\Repos\Mgr\data_random_long\data_modeled_markers\test"

TRAIN_SAVE_PATH = r"C:\Repos\Mgr\data_random_long\data_modeled_markers\complete"
TEST_SAVE_PATH = r"C:\Repos\Mgr\data_random_long\data_modeled_markers\complete"

TRAIN_NAME = r"\train.csv"
TEST_NAME = r"\test.csv"

attempts = [r"\first_attempt", r"\second_attempt", r"\third_attempt"]

def create_dataset(source_path, destination_path):
    csv_data = glob.glob(source_path + "\*.csv")

    first_rows = []

    for csv_path in csv_data:
        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            first_row = next(reader)  # Odczytuje pierwszy wiersz pliku
            first_rows.append(first_row)

    max_length = max(len(l) for l in first_rows)

    # Wypełnienie pozostałych tablic zerami do długości najdłuższej podtablicy
    for l in first_rows:
        while len(l) < max_length:
            l.append(0)

    # Zapisuje pierwsze wiersze do nowego pliku csv
    with open(destination_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(first_rows)  # Zapisuje listę wierszy do pliku


for attempt in attempts:
    train_path = TRAIN_PATH + attempt
    test_path = TEST_PATH + attempt

    train_save_path = TRAIN_SAVE_PATH + attempt + TRAIN_NAME
    test_save_path = TEST_SAVE_PATH + attempt + TEST_NAME

    create_dataset(train_path, train_save_path)
    create_dataset(test_path, test_save_path)