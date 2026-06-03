import pyglet
pyglet.resource.path = ["res"]
pyglet.resource.reindex()

class Application:
    def __init__(self, width, height, caption="Prisma"):
        self.WINDOW_WIDTH = width
        self.WINDOW_HEIGHT = height

        self.Scenes = []

        self.Window = pyglet.window.Window(width, height, caption=caption)

        pyglet.clock.schedule_interval(self.Update, 1/60)

        @self.Window.event
        def on_draw():
            self.Render()

    def Render(self):
        self.Window.clear()
        for scene in self.Scenes:
            if scene.Active:
                scene.Render()

    def Update(self, dt):
        for scene in self.Scenes:
            if scene.Active:
                scene.Update(dt)
