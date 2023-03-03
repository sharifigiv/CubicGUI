import sdl2

class Entry:
    def __init__(self, x, y, width, height, color, rn):
        self.x = x; self.y = y; 
        self.width = width; self.height = height

        self.color = color
        self.rn = rn

        self.text = " "
        self.fontsize = 16

        self.fg = [255, 255, 255, 255]
        self.bg = color

        self.padding_x = 10
        self.padding_y = 10

        self.rect = sdl2.SDL_Rect(self.x, self.y, self.width, self.height)
        self.rn = rn

        self.showing = True
        self.inCharge = False

        self.renderText()

    def renderText(self):
        self.font = sdl2.sdlttf.TTF_OpenFont(str.encode("assets/fonts/font.ttf"), self.fontsize)
        surfaceText = sdl2.sdlttf.TTF_RenderText_Blended(self.font, str.encode(self.text), sdl2.SDL_Color(self.fg[0], self.fg[1], self.fg[2]))
        
        self.rntexture = sdl2.SDL_CreateTextureFromSurface(self.rn, surfaceText)
        self.rectText = sdl2.SDL_Rect(self.x + self.padding_x, self.y + self.padding_y, surfaceText.contents.w, surfaceText.contents.h)

    def update(self, string):
        if self.inCharge:
            self.text += string
            self.renderText()

            print(self.text)

    def draw(self):
        sdl2.SDL_SetRenderDrawColor(self.rn, self.bg[0], self.bg[1], self.bg[2], self.bg[3])
        
        sdl2.SDL_RenderFillRect(self.rn, self.rect)
        sdl2.SDL_RenderCopy(self.rn, self.rntexture , None, self.rectText)

        sdl2.SDL_SetRenderDrawColor(self.rn, 0, 0, 0, 0)