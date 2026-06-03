import pyglet
from pyglet.window import key

Keycodes = pyglet.window.key
Mouse = pyglet.window.mouse

class Event:
    def __init__(self, callback):
        self.Callback = callback
        self.Type = "Event"

class InputHandler:
    def __init__(self, application):
        self._Events = []
        self._App = application
        self.Keys = key.KeyStateHandler()
        self._App.Window.push_handlers(self.Keys)

        @self._App.Window.event
        def on_key_press(symbol, modifiers):
            for event in self._Events:
                if event.Type == "KeyPress":
                    event.Callback(symbol, modifiers)

        @self._App.Window.event
        def on_key_release(symbol, modifiers):
            for event in self._Events:
                if event.Type == "KeyRelease":
                    event.Callback(symbol, modifiers)

        @self._App.Window.event
        def on_mouse_motion(x, y, dx, dy):
            for event in self._Events:
                if event.Type == "MouseMotion":
                    event.Callback(x, y, dx, dy)

        @self._App.Window.event
        def on_mouse_press(x, y, button, modifiers):
            for event in self._Events:
                if event.Type == "MousePress":
                    event.Callback(x, y, button, modifiers)

        @self._App.Window.event
        def on_mouse_release(x, y, button, modifiers):
            for event in self._Events:
                if event.Type == "MouseRelease":
                    event.Callback(x, y, button, modifiers)

        @self._App.Window.event
        def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
            for event in self._Events:
                if event.Type == "MouseDrag":
                    event.Callback(x, y, dx, dy, buttons, modifiers)

        @self._App.Window.event
        def on_text(text):
            for event in self._Events:
                if event.Type == "OnText":
                    event.Callback(text)

    def CreateEvent(self, type, callback):
        newevent = Event(callback)
        newevent.Type = type
        self._Events.append(newevent)
