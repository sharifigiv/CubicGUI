import sys
import ctypes
import sdl2

class CubicGUI:
    def __init__(self):
        sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)

        self.win = None
        self.s = sdl2.SDL_Renderer()

        self.buttons = []

        self.running = True
        
    def update(self):
        # Events  
        event = sdl2.SDL_Event()

        while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == sdl2.SDL_QUIT:
                sdl2.SDL_DestroyWindow(self.win.w)
                sdl2.SDL_Quit()

                self.running = False

    def createWin(self, x, y, width, height, title):
        self.win = Window(x, y, width, height, title) 

    def createButton(self, x, y, width, height):
        b = Button(x, y, width, height, self.s)

        self.buttons.append(b)

        return b

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

class Button:
    def __init__(self, x, y, width, height , rn):
        self.x = x
        self.y = y 

        self.width = width
        self.height = height

        self.bg = ()

        self.border = 0 
        self.borderColor = (0, 0, 0, 0)

        self.radius = 5 

        self.status = True

    def show(self):
        # SDL 2 code
        pass