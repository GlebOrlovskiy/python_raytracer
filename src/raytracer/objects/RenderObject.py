from abc import ABC, abstractmethod
import numpy as np
from raytracer.Ray import Ray
from raytracer.Color import Color


class RenderObject(ABC):
    @abstractmethod
    def intersect(self, ray: Ray) -> tuple[Color | None, np.ndarray | None]:
        pass

    @abstractmethod
    def get_normal_at_point(self, point: np.ndarray) -> np.ndarray:
        pass
