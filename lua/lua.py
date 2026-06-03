
from lupa import LuaRuntime

class LuaEngine:
    def __init__(self) -> None:
        self.Lua = LuaRuntime(unpack_returned_tuples=True)

        self.LuaUpdate = None
        self.LuaDraw = None

    def UpdateGlobals(self):
        if self.Lua.globals()["update"]:
            self.LuaUpdate = self.Lua.globals()["update"]
        if self.Lua.globals()["draw"]:
            self.LuaDraw = self.Lua.globals()["draw"]

    def RegisterGlobalFunction(self, name, func):
        self.Lua.globals()[name] = func
        print("Registered", name)

    def ExecuteLuaFile(self, name):
        with open(name, "r") as f:
            self.Lua.execute(f.read())
        self.UpdateGlobals()

    def Update(self, dt):
        if self.LuaUpdate:
            self.LuaUpdate(dt)

    def Draw(self):
        if self.LuaDraw:
            self.LuaDraw()
