import csv
import re
import glob
import pandas as pd
from pathlib import Path

#data_labels = [406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 433, 434, 435, 442, 445, 446, 448, 449, 451, 453, 455, 456]
data_labels = [406, 407, 409, 410, 411, 412, 414, 415, 416, 417, 418, 419, 433, 434, 435, 442, 445, 446, 448, 449, 451, 453, 455, 456]

for l in range(0, len(data_labels)):

    DIR_PATH = f"C:/Repos/Mgr/data_random_long/data_modeled_markers/short/{data_labels[l]}"
    SAVE_PATH = f"C:/Repos/Mgr/data_random_long/data_modeled_markers/one_line/{data_labels[l]}"

    csv_data = glob.glob(DIR_PATH + "\*.csv")
        
    for csv_path in csv_data:
        try:
            # Pobranie etykiety z nazwy pliku
            regex = re.compile(r'\d+')
            regex.findall(csv_path)
            label = [int(x) for x in regex.findall(csv_path)]

            # Odczytanie danych z pliku csv
            with open(csv_path, 'r') as file:
                reader = csv.reader(file)
                data = list(reader)

            # Sklejenie wszystkich wierszy
            flattened_data = [item for sublist in data for item in sublist]
            flattened_data.insert(0, label[0])

            # Zapisanie sklejonych danych do nowego pliku csv
            save_path = f"{SAVE_PATH}/{Path(csv_path).stem}_one_line.csv"
            with open(save_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(flattened_data)

        except OSError as err:
            print(f"{csv_path}: {err}")