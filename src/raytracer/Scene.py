from raytracer import Color
from raytracer.objects.lights import Light, PointLight
from raytracer.objects.RenderObject import RenderObject


class Scene:
    def __init__(
        self,
        objects: tuple[RenderObject, ...] | tuple[RenderObject] = (),
        lights: tuple[Light, ...] | tuple[Light] = (),
        background_color: Color = Color(0, 0, 0),
        ambient_light: float = 0.2,
    ):
        self.objects = objects
        self.lights = lights
        self.background_color = background_color
        self.ambient_light = ambient_light
