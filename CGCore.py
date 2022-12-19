import sys
import sdl2.ext

class CubicGUI:
    def __init__(self):
        sdl2.ext.init()

        self.win = None

    def update(self):
        if self.win == None:
            return 0 

        # Events
        
        events = sdl2.ext.get_events()

        for event in events:
            if event.type == sdl2.SDL_QUIT:
                self.win.quit()

        self.win.w.refresh()

    def createWin(self, x, y, width, height, title):
        self.win = Window(x, y, width, height, title) 

class Window:
    def __init__(self, x, y, width, height, title):
        self.x = x 
        self.y = y 

        self.width = width
        self.height = height

        self.title = title

        self.w = sdl2.ext.Window(self.title, size=(self.width, self.height), position=(self.x, self.y))

    def show(self):
        self.w.show()

    def quit(self):
        sdl2.ext.quit()