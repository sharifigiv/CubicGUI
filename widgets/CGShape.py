import sdl2
import sdl2.sdlgfx

class Rectangle:
    def __init__(self, x, y, width, height, color, Fillness, rn):
        self.rect = sdl2.SDL_Rect(x, y, width, height)

        self.color = color
        self.rn = rn

        self.showing = True
        self.Fill = Fillness

    def draw(self):
        sdl2.SDL_SetRenderDrawColor(self.rn, self.color[0], self.color[1], self.color[2], self.color[3])

        if not self.Fill:
            sdl2.SDL_RenderDrawRect(self.rn, self.rect)

        else:
            sdl2.SDL_RenderFillRect(self.rn, self.rect)

        sdl2.SDL_SetRenderDrawColor(self.rn, 0, 0, 0, 0)

class Line:
    def __init__(self, x1, y1, x2, y2, color, rn):
        self.x1 = x1; self.y1 = y1
        self.x2 = x2; self.y2 = y2

        self.color = color
        self.rn = rn

        self.showing = True

    def draw(self):
        sdl2.SDL_SetRenderDrawColor(self.rn, self.color[0], self.color[1], self.color[2], self.color[3])

        sdl2.SDL_RenderDrawLine(self.rn, self.x1, self.y1, self.x2, self.y2)
        sdl2.SDL_SetRenderDrawColor(self.rn, 0, 0, 0, 0)

class Circle:
    def __init__(self, x, y, radius, color, rn):
        self.x = x
        self.y = y

        self.r = radius
        self.color = color
        self.rn = rn

        self.showing = True 

        self.color_hex = '0x'
        hexs = []

        for x in self.color:
            chex = str(hex(x))[2:]

            if len(chex) == 1:
                chex = '0' + chex

            hexs.insert(0, chex)

        for h in hexs:
            self.color_hex += h

    def draw(self):
        sdl2.sdlgfx.circleColor(self.rn, self.x, self.y, self.r, eval(self.color_hex))
        # 0xAABBGGRR

        sdl2.SDL_SetRenderDrawColor(self.rn, 0, 0, 0, 0)