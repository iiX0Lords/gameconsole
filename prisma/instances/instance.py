from ..math.vector import Vector2

class Instance:
    def __init__(self, scene):
        self._Position = Vector2(0, 0)
        self._Size = Vector2(100, 100)
        self._Rotation = 0
        self._Colour = (255, 255, 255)
        self._Image = None
        self._Scene = scene

    def Update(self, dt):
        pass
