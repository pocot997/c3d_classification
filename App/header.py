import ezc3d


class HeaderC3D:
    def __init__(self, c3d: ezc3d.c3d):
        self.c3d = c3d

        self.header = c3d.get("header")
        self.points = self.header.get("points") if self.header else None
        self.analogs = self.header.get("analogs") if self.header else None
        self.events = self.header.get("events") if self.header else None

        self.points_size = self.points.get("size") if self.points else None
        self.points_frame_rate = self.points.get("frame_rate") if self.points else None
        self.points_first_frame = (
            self.points.get("first_frame") if self.points else None
        )
        self.points_last_frame = self.points.get("last_frame") if self.points else None
        self.points_frame_count = self.points_last_frame - self.points_first_frame + 1

