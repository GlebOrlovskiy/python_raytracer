import numpy as np

from raytracer import Color, Ray
from raytracer.objects.RenderObject import RenderObject


class Sphere(RenderObject):
    def __init__(self, center: np.ndarray, radius: float, color: Color):
        self.center = center
        self.radius = radius
        self.color = color

    def get_coefficients(self, ray: Ray):
        r = self.radius
        oc = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = 2.0 * oc.dot(ray.direction)
        c = oc.dot(oc) - r * r
        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            return None, None
        else:
            return (-b - discriminant) / (2.0 * a), (-b + discriminant) / (2.0 * a)

    def intersect(self, ray: Ray) -> tuple[Color | None, np.ndarray | None]:
        t1, t2 = self.get_coefficients(ray)
        if t1 is None or t2 is None:
            return None, None
        if t1 >= 1.0:
            return self.color, ray.direction * t1
        if t2 >= 1.0:
            return self.color, ray.direction * t2
        return None, None

    def get_normal_at_point(self, point: np.ndarray) -> np.ndarray:
        vec = point - self.center
        norm = np.linalg.norm(vec)

        if norm <= 0.000001:
            raise ValueError("Некорректная точка")

        return vec / np.linalg.norm(vec)
