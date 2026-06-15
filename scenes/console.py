import prisma
import pyglet
from prisma.core import inputmanager
from prisma.core import time_manager

import lua.lua as Lua

class MainScene(prisma.instances.Scene):
    def __init__(self, app):
        super().__init__(app)
        self.InputManager = inputmanager.InputHandler(self.App)

        self.InputManager.CreateEvent("OnText", self.typed)
        self.InputManager.CreateEvent("KeyPress", self.onkey)
        self.InputManager.CreateEvent("KeyRelease", self.offkey)
        self.string = ""

        testLabel = prisma.instances.Label(self)
        testLabel.Position = prisma.Vector2(0, 580)
        testLabel.Text = ""
        testLabel.TextSize = 20
        testLabel.Font = "Monocraft"
        testLabel.label.anchor_x = "left"
        self.label = testLabel

        self.LuaEngine = Lua.LuaEngine()

        self.grid = []
        for y in range(700):
            row = []
            for x in range(700):
                row.append(None)
            self.grid.append(row)

        self.registerEngineLuaFunctions()

    def registerEngineLuaFunctions(self):
        def spr(sprite, x, y):
            if x < 0 or x >= 700 or y < 0 or y >= 700:
                return
            if not self.grid[y][x]:
                imageSprite = prisma.instances.Sprite(self)
                imageSprite.Image = pyglet.image.load("res/" + sprite)
                imageSprite.Position = prisma.Vector2(x, y)
                self.grid[y][x] = [imageSprite, 1]
            else:
                self.grid[y][x][1] = 1

        self.LuaEngine.RegisterGlobalFunction("spr", spr)

    def updateText(self, newText):
        self.string = newText
        self.label.Text = self.string

    def typed(self, text):
        self.updateText(self.string + text)

    def parseInput(self, text):
        text = text.strip()
        if text[0:3] == "run":
            fileName = text[3:len(text)].strip()
            self.LuaEngine.ExecuteLuaFile(fileName)

    def onkey(self, button, modifiers):
        if button is pyglet.window.key.BACKSPACE:
            self.updateText(self.string[:-1])
        elif button is pyglet.window.key.ENTER:
            self.parseInput(self.string)
            self.updateText("")

    def offkey(self, button, modifiers):
        pass


    def Update(self, dt):
        super().Update(dt)
        self.LuaEngine.Update(dt)

    def Render(self):
        super().Render()
        self.LuaEngine.Render()

        for y in range(700):
            for x in range(700):
                if self.grid[y][x] is not None:
                    if self.grid[y][x][1] == 0:
                        self.grid[y][x][0].Destroy()
                        del self.grid[y][x][0]
                        self.grid[y][x] = None
                    else:
                        self.grid[y][x][1] = 0
