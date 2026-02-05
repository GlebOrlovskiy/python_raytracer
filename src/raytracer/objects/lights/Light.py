from abc import ABC, abstractmethod
import numpy as np


class Light(ABC):
    @abstractmethod
    def get_intensity(self, point: np.ndarray, normal: np.ndarray) -> float:
        pass
