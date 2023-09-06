import os
import csv


class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.directory = os.path.dirname(file_path)
        self.file_full = os.path.basename(file_path)
        self.file_name, self.file_ext = os.path.splitext(self.file_full)
        self.file_name = self.file_name[:self.file_name.find('_')]
        self._validate_file_path()

    def _validate_file_path(self):
        if self.file_ext != ".csv":
            raise OSError(
                f"Required file must have the extension .csv not {self.file_ext}"
            )

    def read_csv(self, file_path: str) -> list:
        result_array = []
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                result_array.append(row)

        return result_array

    def write_euler_csv_without_header(self, data, frame_index: int, data_name: str):
        with open(f"{self.directory}/{self.file_name}_{data_name}.csv", "w", newline="") as f:
            writer = csv.writer(f)

            # Data
            for frame in data:
                angles = []
                angles.append(frame_index)

                for angle in frame:
                    angles.append(angle[0])
                    angles.append(angle[1])
                    angles.append(angle[2])
                writer.writerow(angles)
                frame_index += 1
        print(f"Succesfully saved data to {self.directory}/{self.file_name}_{data_name}.csv")

    def write_euler_csv_with_header(self, data, labels: list, frame_index: int, data_name: str):
        with open(f"{self.directory}/{self.file_name}_{data_name}.csv", "w", newline="") as f:
            writer = csv.writer(f)

            # Header
            header = ["Frame index"]
            for label in labels:
                header.append(f"{label} [X]")
                header.append(f"{label} [Y]")
                header.append(f"{label} [Z]")
            writer.writerow(header)

            # Data
            for frame in data:
                angles = []
                angles.append(frame_index)

                for angle in frame:
                    angles.append(angle[0])
                    angles.append(angle[1])
                    angles.append(angle[2])
                writer.writerow(angles)
                frame_index += 1
        print(f"Succesfully saved data to {self.directory}/{self.file_name}_{data_name}.csv")

    def write_quaternion_csv_without_header(self, data, frame_index: int, data_name: str):
        with open(f"{self.directory}/{self.file_name}_{data_name}.csv", "w", newline="") as f:
            writer = csv.writer(f)

            # Data
            for frame in data:
                angles = []
                angles.append(frame_index)

                for angle in frame:
                    angles.append(angle[0])
                    angles.append(angle[1])
                    angles.append(angle[2])
                    angles.append(angle[3])
                writer.writerow(angles)
                frame_index += 1
        print(f"Succesfully saved data to {self.directory}/{self.file_name}_{data_name}.csv")

    def write_quaternion_csv_with_header(self, data, labels: list, frame_index: int, data_name: str):
        with open(f"{self.directory}/{self.file_name}_{data_name}.csv", "w", newline="") as f:
            writer = csv.writer(f)

            # Header
            header = ["Frame index"]
            for label in labels:
                header.append(f"{label} [w]")
                header.append(f"{label} [i]")
                header.append(f"{label} [j]")
                header.append(f"{label} [k]")
            writer.writerow(header)

            # Data
            for frame in data:
                angles = []
                angles.append(frame_index)

                for angle in frame:
                    angles.append(angle[0])
                    angles.append(angle[1])
                    angles.append(angle[2])
                    angles.append(angle[3])
                writer.writerow(angles)
                frame_index += 1
        print(f"Succesfully saved data to {self.directory}/{self.file_name}_{data_name}.csv")
