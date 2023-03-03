import sdl2

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