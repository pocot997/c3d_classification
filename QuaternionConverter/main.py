import glob
import numpy as np
from scipy.spatial.transform import Rotation as R
from file_manager import FileManager


# This software can read only csv data with headers!
DIR_PATH = r"C:\Users\Szkolenie\Desktop\Obrobione"
INCLUDE_HEADER = True
EULER_TO_QUATERNION = True


def quaternion_to_euler(file_path:str, include_header:bool):
    file_manager = FileManager(file_path)
    file_data = file_manager.read_csv(file_path)

    quaternion_data = []
    header = file_data[0]
    just_data = file_data[1:]
    first_frame_index = int(just_data[0][0])

    # Extract joints names
    joints_labels = []
    for i in range(int(len(header[1:]) / 4)):
        joints_labels.append(header[i * 4 + 1][:-4])

    # Read quaternions
    for i in range(len(just_data)):
        quaternion_data.append([])
        for j in range(int(len(just_data[1][1:]) / 4)):
            quaternion_data[i].append([float(just_data[i][j * 4 + 1]), float(just_data[i][j * 4 + 2]), float(just_data[i][j * 4 + 3]), float(just_data[i][j * 4 + 4])])

    # Convert to eulers
    euler_data = []
    for frame in quaternion_data:
        new_frame = []
        for q in frame:
            quaternion = [q[0], q[1], q[2], q[3]]
            r = R.from_quat(quaternion)
            euler_angles = r.as_euler('xyz', degrees=True)
            
            new_frame.append([euler_angles[0], euler_angles[1], euler_angles[2]])
        euler_data.append(new_frame)

    # Save to csv
    if include_header:
        file_manager.write_euler_csv_with_header(euler_data, joints_labels, first_frame_index, "euler")
    else:
        file_manager.write_euler_csv_without_header(euler_data, first_frame_index, "euler_no_header")


def euler_to_quaternion(file_path:str, include_header:bool):
    file_manager = FileManager(file_path)
    file_data = file_manager.read_csv(file_path)

    euler_data = []
    header = file_data[0]
    just_data = file_data[1:]
    first_frame_index = int(just_data[0][0])

    # Extract joints names
    joints_labels = []
    for i in range(int(len(header[1:]) / 3)):
        joints_labels.append(header[i * 3 + 1][:-4])

    # Read eulers
    for i in range(len(just_data)):
        euler_data.append([])
        for j in range(int(len(just_data[1][1:]) / 3)):
            euler_data[i].append([float(just_data[i][j * 3 + 1]), float(just_data[i][j * 3 + 2]), float(just_data[i][j * 3 + 3])])

    # Convert to quaternions
    quaternion_data = []
    for frame in euler_data:
        new_frame = []
        for angle in frame:
            x = angle[0]
            y = angle[1]
            z = angle[2]

            r = R.from_euler('xyz', [x, y, z], degrees=True)
            quaternion = r.as_quat()
            new_frame.append([quaternion[3], quaternion[0], quaternion[1], quaternion[2]])
        quaternion_data.append(new_frame)

    # Save to csv
    if include_header:
        file_manager.write_quaternion_csv_with_header(quaternion_data, joints_labels, first_frame_index, "quaternion")
    else:
        file_manager.write_quaternion_csv_without_header(quaternion_data, first_frame_index, "quaternion_no_header")


if __name__ == '__main__':
    csv_files = glob.glob(DIR_PATH + "\*.csv")
    
    if EULER_TO_QUATERNION:
        for csv_file in csv_files:
            euler_to_quaternion(csv_file, INCLUDE_HEADER)
    else:
        for csv_file in csv_files:
            quaternion_to_euler(csv_file, INCLUDE_HEADER)