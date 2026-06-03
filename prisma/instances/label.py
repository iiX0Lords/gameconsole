import pyglet
from ..math.vector import Vector2
from .instance import Instance

class Label(Instance):
    def __init__(self, scene):
        super().__init__(scene)
        self._Batch = self._Scene.Batch
        self.label = pyglet.text.Label('Label', font_name='Arial', font_size=36, x=0, y=0, anchor_x='center', anchor_y='center', batch=self._Batch)

        self._Position = Vector2(0, 0)

        self._Scene.Children.append(self)

    @property
    def Position(self):
        return self._Position
    @Position.setter
    def Position(self, value):
        self._Position = value

        self.label.x = value.x
        self.label.y = value.y

    @property
    def Text(self):
        return self.label.text

    @Text.setter
    def Text(self, text):
        self.label.text = text

    @property
    def Colour(self):
        return self.label.color

    @Colour.setter
    def Colour(self, colour):
        self.label.color = colour

    @property
    def Font(self):
        return self.label.font_name

    @Font.setter
    def Font(self, font):
        self.label.font_name = font

    @property
    def TextSize(self):
        return self.label.font_size

    @TextSize.setter
    def TextSize(self, fontSize):
        self.label.font_size = fontSize

    def Destroy(self):
        if self._Batch is None:
            return
        self.label.delete()
        self._Scene.Children.remove(self)

    def AssignToRoot(self, instance):
        if hasattr(instance, "Batch"):
            self.label.batch = instance.Batch
            self._Batch = instance.Batch
        else:
            print("Instance does not have Batch")
