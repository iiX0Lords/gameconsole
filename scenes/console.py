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
        testLabel.Font = "Arial"
        testLabel.label.anchor_x = "left"
        self.label = testLabel

        self.LuaEngine = Lua.LuaEngine()

        self.drawQueue = []
        self.textures = {} 
        self.activeSprites = []
        self.spritePool = []

        self.registerEngineLuaFunctions()

        self.running = False

        self.keys = pyglet.window.key.KeyStateHandler()
        app.Window.push_handlers(self.keys)

    def get_texture(self, sprite_name):
        """Caches textures on demand so we don't load from disk every frame."""
        if sprite_name not in self.textures:
            self.textures[sprite_name] = pyglet.image.load("res/" + sprite_name)
        return self.textures[sprite_name]

    def registerEngineLuaFunctions(self):
        def cls():
            self.drawQueue.clear()
            
        self.LuaEngine.RegisterGlobalFunction("cls", cls)

        def spr(sprite, x, y):
            self.drawQueue.append((sprite, x, y))

        self.LuaEngine.RegisterGlobalFunction("spr", spr)

        def btn(keycode):
            if keycode == "left":
                return self.keys[pyglet.window.key.LEFT] or self.keys[pyglet.window.key.A]
            elif keycode == "right":
                return self.keys[pyglet.window.key.RIGHT] or self.keys[pyglet.window.key.D]
            elif keycode == "up":
                return self.keys[pyglet.window.key.UP] or self.keys[pyglet.window.key.W]
            elif keycode == "down":
                return self.keys[pyglet.window.key.DOWN] or self.keys[pyglet.window.key.S]
            elif keycode == "z":
                return self.keys[pyglet.window.key.Z]
            elif keycode == "x":
                return self.keys[pyglet.window.key.X]
            elif keycode == "space":
                return self.keys[pyglet.window.key.SPACE]

        self.LuaEngine.RegisterGlobalFunction("btn", btn)

    def updateText(self, newText):
        self.string = newText
        self.label.Text = self.string

    def typed(self, text):
        if self.running:
            return
        self.updateText(self.string + text)

    def parseInput(self, text):
        text = text.strip()
        if text[0:3] == "run":
            fileName = text[3:len(text)].strip()
            self.LuaEngine.ExecuteLuaFile(fileName + ".lua")
            self.running = True

    def onkey(self, button, modifiers):
        if button is pyglet.window.key.BACKSPACE:
            if not self.running:
                self.updateText(self.string[:-1])
            else:
                self.running = False
                self.drawQueue.clear()
                self.LuaEngine.LuaDraw = None
                self.LuaEngine.LuaUpdate = None
        elif button is pyglet.window.key.ENTER:
            self.parseInput(self.string)
            self.updateText("")

    def offkey(self, button, modifiers):
        pass

    def Update(self, dt):
        super().Update(dt)
        self.LuaEngine.Update(dt)

    def Render(self):

        for s in self.activeSprites:
            s.Destroy()
        self.activeSprites.clear()

        self.LuaEngine.Render()

        for spriteName, x, y in self.drawQueue:
            tex = self.get_texture(spriteName)

            s = prisma.instances.Sprite(self)
            s.Image = tex
            s.Position = prisma.Vector2(x, y)
            s.Size = prisma.Vector2(tex.width * 2, tex.height * 2)
            
            self.activeSprites.append(s)

        self.drawQueue.clear()

        super().Render()