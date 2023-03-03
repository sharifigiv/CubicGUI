import sdl2 
import sdl2.sdlimage

class Image:
    def __init__(self, x, y, width, height, file, rn):
        self.x = x
        self.y = y

        self.img = sdl2.sdlimage.IMG_LoadTexture(rn, str.encode(file))
        sdl2.SDL_QueryTexture(img, None, None, width, height)

        self.rect = sdl2.SDL_Rect(x, y, width * 2, height * 2)
        self.rn = rn

        self.showing = True

    def draw(self):
        sdl2.SDL_RenderCopy(self.rn, self.img, None, self.rect)
        sdl2.SDL_SetRenderDrawColor(self.rn, 0, 0, 0, 0)