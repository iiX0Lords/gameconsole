import pyglet

class Scene:
    def __init__(self, application):
        self.Batch = pyglet.graphics.Batch()
        self.Active = False
        self.Children = []
        self.App = application
        self.Window = self.App.Window
        self.App.Scenes.append(self)

    def Render(self):
        self.Batch.draw()

    def Update(self, dt):
        for child in self.Children:
            child.Update(dt)
