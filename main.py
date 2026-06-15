import pyglet
import prisma
from scenes import console as console

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
main = prisma.core.Application(WINDOW_WIDTH, WINDOW_HEIGHT, "Cartridge")

consoleScene = console.MainScene(main)
consoleScene.Active = True

pyglet.app.run()
