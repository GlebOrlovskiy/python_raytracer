import numpy as np

from raytracer.Ray import Ray


class Camera:
    def __init__(
        self,
        position: np.ndarray,
        look_at: np.ndarray,
        up_vector: np.ndarray,
        fov: float,
        distanсe_from_pos_to_viewport: float,
        viewport_width: float = 1.0,
        viewport_height: float = 1.0,
        canvas_width: int = 1,
        canvas_height: int = 1,
    ):
        self.position = position
        self.look_at = look_at
        self.up_vector = up_vector
        self.fov = fov
        self.viewport_width = viewport_width
        self.viewport_height = viewport_height
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.distanсe_from_pos_to_viewport = distanсe_from_pos_to_viewport

    def canvas_coord_to_viewport(
        self, canvas_x: int, canvas_y: int
    ) -> tuple[float, float]:
        viewport_x = (canvas_x / self.canvas_width) * self.viewport_width
        viewport_y = (canvas_y / self.canvas_height) * self.viewport_height
        return viewport_x, viewport_y

    def get_ray(self, canvas_x: int, canvas_y: int) -> Ray:
        viewport_x, viewport_y = self.canvas_coord_to_viewport(canvas_x, canvas_y)
        direction = np.array(
            [viewport_x, viewport_y, self.distanсe_from_pos_to_viewport]
        ) - np.array(self.position)
        return Ray(self.position, direction)
