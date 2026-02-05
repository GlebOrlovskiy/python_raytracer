class Color:
    def __init__(self, r: int = 0, g: int = 0, b: int = 0):
        self.r = max(0, min(255, r))
        self.g = max(0, min(255, g))
        self.b = max(0, min(255, b))

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __rmul__(self, scalar):
        return Color(int(self.r * scalar), int(self.g * scalar), int(self.b * scalar))

    def __iter__(self):
        return iter((self.r, self.g, self.b))

    def __str__(self):
        return f"Color({self.r}, {self.g}, {self.b})"
