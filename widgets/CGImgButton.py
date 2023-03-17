import sdl2 
import sdl2.sdlimage
from ctypes import pointer, c_int

class ImgButton:
    def __init__(self, x, y, width, height, file, rn, command):
        self.x = x
        self.y = y

        self.img = sdl2.sdlimage.IMG_LoadTexture(rn, str.encode(file))

        w = pointer(c_int(width))
        h = pointer(c_int(height))

        sdl2.SDL_QueryTexture(self.img, None, None, w, h)

        self.rect = sdl2.SDL_Rect(x, y, width * 2, height * 2)

        self.borderWidth = 0
        self.borderColor = [235, 64, 52, 255]

        self.status = True
        self.hovering = False

        self.command = command

        self.showing = True
        self.rn = rn

    def draw(self):
        sdl2.SDL_RenderCopy(self.rn, self.img, None, self.rect)

        sdl2.SDL_SetRenderDrawColor(self.rn, self.borderColor[0], self.borderColor[1], self.borderColor[2], self.borderColor[3])

        for i in range(1, self.borderWidth + 1):
            rectBorder = sdl2.SDL_Rect(self.x - i, self.y - i, self.width + i * 2 , self.height + i * 2)

            sdl2.SDL_RenderDrawRect(self.rn, rectBorder)

        sdl2.SDL_SetRenderDrawColor(self.rn, 0, 0, 0, 0)