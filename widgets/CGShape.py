import sdl2

class Rectangle:
    def __init__(self, x, y, width, height, color, rn):
        self.rect = sdl2.SDL_Rect(x, y, width, height)

        self.color = color
        self.rn = rn

        self.showing = True

    def draw(self):
        sdl2.SDL_SetRenderDrawColor(self.rn, self.color[0], self.color[1], self.color[2], self.color[3])

        sdl2.SDL_RenderDrawRect(self.rn, self.rect)
        sdl2.SDL_SetRenderDrawColor(self.rn, 0, 0, 0, 0)

class Line:
    def __init__(self, x1, y1, x2, y2, color, rn):
        self.x1 = x1; self.y1 = y1
        self.x2 = x2; self.y2 = y2

        self.color = color
        self.rn = rn

        elf.showing = True

    def draw(self):
        sdl2.SDL_SetRenderDrawColor(self.rn, self.color[0], self.color[1], self.color[2], self.color[3])

        sdl2.SDL_RenderDrawLine(self.rn, self.x1, self.y1, self.x2, self.y2)
        sdl2.SDL_SetRenderDrawColor(self.rn, 0, 0, 0, 0)