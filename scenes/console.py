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
