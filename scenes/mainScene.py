import prisma
import pyglet
from prisma.core import inputmanager
#TODO make assetmanager class

class MainScene(prisma.instances.Scene):
    def __init__(self, app):
        super().__init__(app)
        self.InputManager = inputmanager.InputHandler(self.App)

        self.InputManager.CreateEvent("MousePress", self.pressed)
    
    def spawn(self, x, y):
        sprite = prisma.instances.Sprite(self)
        sprite.Image = pyglet.image.load("res/test.jpg")
        sprite.Position = prisma.Vector2(x, y)

    def pressed(self, x, y, button, modifiers):
        if button == 1:
            self.spawn(x, y)
        elif button == 2:
            for sprite in self.Children:
                if hasattr(sprite, "Destroy"):
                    sprite.Destroy()
                    print(sprite)