import ezc3d


class DataC3D:
    def __init__(self, c3d: ezc3d.c3d):
        self.c3d = c3d

        self.data = self.c3d.get("data")
        self.points = self.data.get("points") if self.data else None
        self.meta_points = self.data.get("meta_points") if self.data else None
        self.analogs = self.data.get("analogs") if self.data else None

        self.point_data = PointDataC3D(self.points)


class PointDataC3D:
    # >>> Constructor <<<
    def __init__(self, point_data):
        self.point_data = point_data

    # >>> Data methods <<<
    def get_data_by_indices(self, indices: list, frame_count: int):
        data = []
        for frame in range(frame_count):
            data.append([])
            for index in indices:
                data[frame].append(
                    [
                        self.point_data[0][index][frame],
                        self.point_data[1][index][frame],
                        self.point_data[2][index][frame],
                    ]
                )
        return data
