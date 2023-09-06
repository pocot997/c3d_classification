import ezc3d

from data_type import DataType
from file_management import FileManager
from header import HeaderC3D
from parameters import ParametersC3D
from data import DataC3D

MARKERS_COUNT = 39

class Scraper:
    def __init__(self, file_path):
        self.file_path = file_path

        # Containers initialization
        try:
            self.file_manager = FileManager(file_path)
            self.c3d = ezc3d.c3d(file_path)
        except OSError as err:
            raise err

        self.header = HeaderC3D(self.c3d)
        self.parameters = ParametersC3D(self.c3d, MARKERS_COUNT, self.header.points_size)
        self.point_info = self.parameters.point_info
        self.data = DataC3D(self.c3d)
        self.point_data = self.data.point_data


    def report_data_to_csv(self, data_type: DataType, include_header: bool):
        labels = []
        indices = []
        data_name = ""

        # Markers
        if data_type is DataType.MARKERS:
            labels = self.point_info.markers
            indices = self.point_info.get_markers_indices()
            data_name = "markers"

        # Virtual markers
        elif data_type is DataType.VIRTUAL_MARKERS:
            labels = self.point_info.virtual_markers
            indices = self.point_info.get_virtual_markers_indices()
            data_name = "virtual_markers"

        # Modeled markers
        elif data_type is DataType.MODELED_MARKERS:
            labels = self.point_info.modeled_markers
            indices = self.point_info.get_modeled_markers_indices()
            data_name = "modeled_markers"

        # Angles
        elif data_type is DataType.ANGLES:
            labels = self.point_info.angles
            indices = self.point_info.get_angles_indices()
            data_name = "angles"

        # Forces
        elif data_type is DataType.FORCES:
            labels = self.point_info.forces
            indices = self.point_info.get_forces_indices()
            data_name = "forces"

        # Moments
        elif data_type is DataType.MOMENTS:
            labels = self.point_info.moments
            indices = self.point_info.get_moments_indices()
            data_name = "moments"

        # Powers
        elif data_type is DataType.POWERS:
            labels = self.point_info.powers
            indices = self.point_info.get_powers_indices()
            data_name = "powers"

        self._get_data(labels, indices, data_name, include_header)


    def _get_data(self, labels: list, indices: list, data_name: str, include_header: bool):
        # Frame count
        first_frame = self.header.points_first_frame
        frame_count = self.header.points_frame_count

        # Angle data
        data = self.point_data.get_data_by_indices(indices, frame_count)

        # Writing to csv
        if include_header:
            self.file_manager.write_csv_with_header(data, labels, first_frame, data_name)
        else:
            self.file_manager.write_csv(data, first_frame, data_name)
