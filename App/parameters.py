import ezc3d
from c3d_exception import C3DError

class ParametersC3D:
    def __init__(self, c3d: ezc3d.c3d, markers_count: int, points_size: int):
        self.c3d = c3d

        self.parameters = c3d.get("parameters")
        self.trial = self.parameters.get("TRIAL") if self.parameters else None
        self.subjects = self.parameters.get("SUBJECTS") if self.parameters else None
        self.point = self.parameters.get("POINT") if self.parameters else None
        self.analog = self.parameters.get("ANALOG") if self.parameters else None
        self.force_platform = (
            self.parameters.get("FORCE_PLATFORM") if self.parameters else None
        )
        self.event_context = (
            self.parameters.get("EVENT_CONTEXT") if self.parameters else None
        )
        self.event = self.parameters.get("EVENT") if self.parameters else None
        self.manufacturer = (
            self.parameters.get("MANUFACTURER") if self.parameters else None
        )
        self.analysis = self.parameters.get("ANALYSIS") if self.parameters else None
        self.processing = self.parameters.get("PROCESSING") if self.parameters else None

        self.point_info = PointInfoC3D(self.point, markers_count, points_size)


class PointInfoC3D:
    # >>> Constructor <<<
    def __init__(self, point_info, markers_count: int, points_size: int):
        self.point_info = point_info
        self.markers_count = markers_count
        self.points_size = points_size

        self.used = point_info.get("USED")
        self.frames = point_info.get("FRAMES", {}).get("value")
        self.scale = point_info.get("SCALE", {}).get("value")
        self.rate = point_info.get("RATE", {}).get("value")
        self.movie_delay = point_info.get("MOVIE_DELAY", {}).get("value")
        self.movie_id = point_info.get("MOVIE_ID", {}).get("value")
        self.x_screen = point_info.get("X_SCREEN", {}).get("value")
        self.y_screen = point_info.get("Y_SCREEN", {}).get("value")
        self.units = point_info.get("UNITS", {}).get("value")
        self.angle_units = point_info.get("ANGLE_UNITS", {}).get("value")
        self.force_units = point_info.get("FORCE_UNITS", {}).get("value")
        self.moment_units = point_info.get("MOMENT_UNITS", {}).get("value")
        self.power_units = point_info.get("POWER_UNITS", {}).get("value")
        self.modeled_marker_units = point_info.get("MODELED_MARKER_UNITS")
        self.labels = point_info.get("LABELS", {}).get("value")
        self.descriptions = point_info.get("DESCRIPTIONS", {}).get("value")
        self.angles = point_info.get("ANGLES", {}).get("value")
        self.forces = point_info.get("FORCES", {}).get("value")
        self.moments = point_info.get("MOMENTS", {}).get("value")
        self.powers = point_info.get("POWERS", {}).get("value")
        self.modeled_markers = point_info.get("MODELED_MARKERS", {}).get("value")
        self.type_groups = point_info.get("TYPE_GROUPS", {}).get("value")
        self.data_start = point_info.get("DATA_START", {}).get("value")


        # Setup markers
        try:
            self.markers = []
            for index in range(self.markers_count):
                self.markers.append(self.labels[index])
        except IndexError:
            raise C3DError("Incorrect number of real markers")

        # Setup virtual markers
        self.virtual_markers = []
        count = self.try_get_indices(self.modeled_markers)
        count += self.try_get_indices(self.angles)
        count += self.try_get_indices(self.forces)
        count += self.try_get_indices(self.moments)
        count += self.try_get_indices(self.powers)

        for index in range(self.points_size - self.markers_count - count):
            self.virtual_markers.append(self.labels[index + self.markers_count])

    # >>> Indices methods <<<
    def _get_indices_by_labels(self, labels: list) -> list:
        indices = []
        for label in labels:
            indices.append(self.labels.index(label))
        return indices

    def get_markers_indices(self) -> list:
        if len(self.markers) == 0:
            raise C3DError("Markers doesn't exist in this file")
        try:
            return self._get_indices_by_labels(self.markers)
        except ValueError:
            raise C3DError("Markers doesn't exist in this file")

    def get_virtual_markers_indices(self) -> list:
        if len(self.virtual_markers) == 0:
            raise C3DError("Virtual markers doesn't exist in this file")
        try:
            return self._get_indices_by_labels(self.virtual_markers)
        except ValueError:
            raise C3DError("Virtual markers doesn't exist in this file")

    def get_modeled_markers_indices(self) -> list:
        if self.modeled_markers is None:
            raise C3DError("Modeled markers doesn't exist in this file")
        try:
            return self._get_indices_by_labels(self.modeled_markers)
        except ValueError:
            raise C3DError("Modeled markers doesn't exist in this file")

    def get_angles_indices(self) -> list:
        if self.angles is None:
            raise C3DError("Angles doesn't exist in this file")
        try:
            return self._get_indices_by_labels(self.angles)
        except ValueError:
            raise C3DError("Angles doesn't exist in this file")

    def get_forces_indices(self) -> list:
        if self.forces is None:
            raise C3DError("Forces doesn't exist in this file")
        try:
            return self._get_indices_by_labels(self.forces)
        except ValueError:
            raise C3DError("Forces doesn't exist in this file")

    def get_moments_indices(self) -> list:
        if self.moments is None:
            raise C3DError("Moments doesn't exist in this file")
        try:
            return self._get_indices_by_labels(self.moments)
        except ValueError:
            raise C3DError("Moments doesn't exist in this file")

    def get_powers_indices(self) -> list:
        if self.powers is None:
            raise C3DError("Powers doesn't exist in this file")
        try:
            return self._get_indices_by_labels(self.powers)
        except ValueError:
            raise C3DError("Powers doesn't exist in this file")

    def try_len(self, container: list) -> int:
        try:
            return len(container)
        except TypeError:
            return 0
        
    def try_get_indices(self, labels: list) -> int:
        try:
            return self.try_len(self._get_indices_by_labels(labels))
        except ValueError:
            return 0 
        except TypeError:
            return 0
