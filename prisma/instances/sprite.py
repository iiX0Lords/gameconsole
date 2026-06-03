import pyglet
#from ..math.vector import Vector2
from .instance import Instance

class Sprite(Instance):
    def __init__(self, scene):
        super().__init__(scene)
        self._Batch = self._Scene.Batch

        placeholder = pyglet.image.SolidColorImagePattern((0,0,0,0)).create_image(1,1)
        self._visual = pyglet.sprite.Sprite(img=placeholder, x=0, y=0, batch=self._Batch)
        self._visual.visible = False

        self._Scene.Children.append(self)

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, value):
        self._Image = value

        try:
            self._Image.anchor_x = self._Image.width // 2
            self._Image.anchor_y = self._Image.height // 2
        except Exception:
            pass

        self._visual = pyglet.sprite.Sprite(
            img=self._Image,
            x=0, y=0,
            batch=self._Batch
        )

        scale_x = self._Size.x / max(1, self._Image.width)   
        scale_y = self._Size.y / max(1, self._Image.height)  
        self._visual.update(scale_x=scale_x, scale_y=scale_y)

        self._visual.rotation = self._Rotation
        try:
            self._visual.color = self._Colour[:3]
        except Exception:
            pass

        self._visual.visible = True
        self.Position = self._Position

    @property
    def Size(self):
        return self._Size
    @Size.setter
    def Size(self, value):
        self._Size = value
        if self._Image:
            sx = value.x / max(1, self._Image.width)  
            sy = value.y / max(1, self._Image.height) 
            self._visual.update(scale_x=sx, scale_y=sy)
            self.Position = self._Position

    @property
    def Position(self):
        return self._Position
    @Position.setter
    def Position(self, value):
        self._Position = value

        if not hasattr(self, "_visual") or self._visual is None:
            return

        if self._Image:
            adjusted_x = value.x  
            adjusted_y = value.y  

            self._visual.update(x=adjusted_x, y=adjusted_y)
        else:
            self._visual.update(x=value.x, y=value.y) 

    @property
    def Rotation(self):
        return self._Rotation
    @Rotation.setter
    def Rotation(self, value):
        self._Rotation = value
        if hasattr(self, "_visual") and self._visual is not None:
            self._visual.rotation = value

    @property
    def Colour(self):
        return self._Colour
    @Colour.setter
    def Colour(self, value):
        self._Colour = value
        try:
            self._visual.color = value[:3]
        except Exception:
            pass

    def Destroy(self):
        if self._Batch is None:
            return
        self._visual.delete()
        self._Scene.Children.remove(self)

    def AssignToRoot(self, instance):
        if hasattr(instance, "Batch"):
            self._visual.batch = instance.Batch
            self._Batch = instance.Batch
        else:
            print("Instance does not have Batch")