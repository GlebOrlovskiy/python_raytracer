import numpy as np

from raytracer import Camera, Color, Scene


class Render:
    def __init__(self, width: int, height: int, scene: Scene, camera: Camera):
        self.width = width
        self.height = height
        self.scene = scene
        self.camera = camera
        self.canvas: list[list[tuple[Color, float]]] = [
            [(scene.background_color, float("inf")) for _ in range(height)]
            for _ in range(width)
        ]

    def update(self, pixels):
        for y in range(self.height):
            for x in range(self.width):
                self.canvas[x][y] = self.get_color_and_depth(
                    x - self.width // 2, -y + self.height // 2
                )
                pixels[x, y] = tuple(self.canvas[x][y][0])

    def get_intensity_at_point(self, point, normal):
        intensity = self.scene.ambient_light
        for light in self.scene.lights:
            intensity += light.get_intensity(point, normal)
        return min(1, intensity)

    def get_color_and_depth(self, x: int, y: int) -> tuple[Color, float]:
        color = self.scene.background_color
        depth = float("inf")
        closest_from_camera_pos_to_point = None
        intersection_obj = None
        for obj in self.scene.objects:
            obj_color, from_camera_pos_to_point = obj.intersect(
                self.camera.get_ray(x, y)
            )
            if obj_color is not None and from_camera_pos_to_point is not None:
                obj_depth = np.linalg.norm(from_camera_pos_to_point)
                if obj_depth < depth:
                    depth = obj_depth
                    color = obj_color
                    intersection_obj = obj
                    closest_from_camera_pos_to_point = from_camera_pos_to_point

        intensity = 1.0
        if intersection_obj is not None:
            intersection_point = self.camera.position + closest_from_camera_pos_to_point
            normal = intersection_obj.get_normal_at_point(intersection_point)
            intensity = self.get_intensity_at_point(intersection_point, normal)
        return intensity * color, float(depth)
