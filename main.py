import pyglet
import prisma
from scenes import console as console
from pyglet.gl import glTexParameteri, GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_TEXTURE_MIN_FILTER, GL_NEAREST

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
main = prisma.core.Application(WINDOW_WIDTH, WINDOW_HEIGHT, "Cartridge")

glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

consoleScene = console.MainScene(main)
consoleScene.Active = True

pyglet.app.run()
