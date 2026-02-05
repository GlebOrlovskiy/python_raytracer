import numpy as np
from .Light import Light


class PointLight(Light):
    def __init__(self, position: np.ndarray, intensity: float):
        self.position = position
        self.intensity = intensity

    def get_intensity(self, point: np.ndarray, normal: np.ndarray) -> float:
        light_dir = self.position - point
        light_distance = np.linalg.norm(light_dir)
        light_dir = light_dir / light_distance
        intensity = (
            self.intensity
            * max(0.0, normal.dot(light_dir))
            / (light_distance**2 + 1e-6)
        )
        return float(intensity)
