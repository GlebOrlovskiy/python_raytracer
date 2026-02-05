import sys
from pathlib import Path

import numpy as np
from loguru import logger
from PIL import Image

if __name__ == "__main__" and __package__ is None:
    sys.path.insert(0, str(Path(__file__).parent.parent))
    __package__ = "raytracer"

from raytracer import Camera, Color, Render, Scene
from raytracer.objects import Sphere
from raytracer.objects.lights import PointLight


def main():
    width, height = 1920, 1080
    img = Image.new("RGB", (width, height), (0, 0, 0))
    pixels = img.load()

    scene = Scene(
        objects=(
            Sphere(
                center=np.array([0.0, 0.0, 5.0]), radius=0.5, color=Color(255, 0, 0)
            ),
            Sphere(
                center=np.array([0.4, 0.0, 3.0]), radius=0.2, color=Color(0, 255, 0)
            ),
            Sphere(
                center=np.array([-0.4, 0.0, 3.0]), radius=0.2, color=Color(0, 0, 255)
            ),
        ),
        lights=(
            PointLight(position=np.array([5.0, 0, 1.0]), intensity=50.0),
        ),
    )
    camera = Camera(
        position=np.array([0.0, 0.0, -1.0]),
        look_at=np.array([0.0, 0.0, 0.0]),
        up_vector=np.array([0.0, 1.0, 0.0]),
        fov=90,
        distanсe_from_pos_to_viewport=1.0,
        viewport_width=width / np.sqrt(width**2 + height**2),
        viewport_height=height / np.sqrt(width**2 + height**2),
        canvas_width=width,
        canvas_height=height,
    )
    renderer = Render(width, height, scene, camera)
    renderer.update(pixels)

    img.save("output.png")


if __name__ == "__main__":
    logger.add("file.log", rotation="10 MB")
    main()
