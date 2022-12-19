import sys
import ctypes
import sdl2

class CubicGUI:
    def __init__(self):
        sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)

        self.win = None
        self.running = True
        
    def update(self):
        if self.win == None:
            return 0 

        # Events  
        event = sdl2.SDL_Event()

        while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == sdl2.SDL_QUIT:
                sdl2.SDL_DestroyWindow(self.win.w)
                sdl2.SDL_Quit()

                self.running = False

    def createWin(self, x, y, width, height, title):
        self.win = Window(x, y, width, height, title) 

class Window:
    def __init__(self, x, y, width, height, title):
        self.x = x 
        self.y = y 

        self.width = width
        self.height = height

        self.title = title

        self.w = sdl2.SDL_CreateWindow(bytes(self.title, 'utf-8'), self.x, self.y, self.width, self.height, sdl2.SDL_WINDOW_SHOWN)

    def quit(self):
        sdl2.SDL_DestroyWindow(self.w)