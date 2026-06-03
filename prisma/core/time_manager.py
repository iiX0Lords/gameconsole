import pyglet

@staticmethod
def ScheduleInterval(callback, interval, scene=None):
    def checkThenCallback(*args):
        if scene is None:
            callback(*args)
        else:
            if scene.Active:
                callback(*args)
    return pyglet.clock.schedule_interval(checkThenCallback, interval)