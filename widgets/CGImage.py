import sdl2 
import sdl2.sdlimage
from ctypes import pointer, c_int

class Image:
    def __init__(self, x, y, width, height, file, rn):
        self.x = x
        self.y = y

        self.img = sdl2.sdlimage.IMG_LoadTexture(rn, str.encode(file))

        w = pointer(c_int(width))
        h = pointer(c_int(height))

        sdl2.SDL_QueryTexture(self.img, None, None, w, h)

        self.rect = sdl2.SDL_Rect(x, y, width * 2, height * 2)
        self.rn = rn

        self.showing = True

    def draw(self):
        sdl2.SDL_RenderCopy(self.rn, self.img, None, self.rect)
        sdl2.SDL_SetRenderDrawColor(self.rn, 0, 0, 0, 0)