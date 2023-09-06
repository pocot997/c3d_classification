import os
import shutil
import random

DIR_PATH = r"C:\Repos\Mgr\data_random_long\data_modeled_markers\one_line"
TRAIN_PATH = r"C:\Repos\Mgr\data_random_long\data_modeled_markers\train"
TEST_PATH = r"C:\Repos\Mgr\data_random_long\data_modeled_markers\test"

#data_labels = [406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 433, 434, 435, 442, 445, 446, 448, 449, 451, 453, 455, 456]
data_labels = [406, 407, 409, 410, 411, 412, 414, 415, 416, 417, 418, 419, 433, 434, 435, 442, 445, 446, 448, 449, 451, 453, 455, 456]
test_file_number = 4

attempts = [r"\first_attempt", r"\second_attempt", r"\third_attempt"]

# Kopiowanie wskazanych plików
def copy_files(file_list, source_folder, destination_folder):
    for file_name in file_list:
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.copy2(source_path, destination_path)

# Usuwanie wskazanych plików
def delete_files(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        if os.path.isfile(file_path):
            os.remove(file_path)

for attempt in attempts:
    train_destination_path = TRAIN_PATH + attempt
    test_destination_path = TEST_PATH + attempt
    
    delete_files(train_destination_path)
    delete_files(test_destination_path)

    for l in range(0, len(data_labels)):

        source_path = os.path.join(DIR_PATH, f"{data_labels[l]}")

        all_files = os.listdir(source_path)

        # Losowe wybranie plików testowych
        test_files = random.sample(all_files, test_file_number)

        # Utworzenie plików treningowych jako różnicy zbiorów wszystkich plików i plików testowych
        train_files = [file for file in all_files if file not in test_files]

        copy_files(train_files, source_path, train_destination_path)
        copy_files(test_files, source_path, test_destination_path)