class Entry:
    def __init__(self, x, y, width, height, color, rn):
        self.x = x; self.y = y; 
        self.width = width; self.height = height

        self.color = color
        self.rn = rn

        self.text = ""
        self.font = 16

        self.fg = [0, 0, 0, 255]
        self.bg = [255, 255, 255, 255]

        self.rect = sdl2.SDL_Rect(self.x, self.y, self.width, self.height)
        self.rn = rn

        self.showing = True
        self.inCharge = False

        self.renderText()

    def renderText(self):
        self.font = sdl2.sdlttf.TTF_OpenFont(str.encode("assets/fonts/font.ttf"), self.fontsize)
        surfaceText = sdl2.sdlttf.TTF_RenderText_Blended(self.font, str.encode(self.text), sdl2.SDL_Color(self.fg[0], self.fg[1], self.fg[2]))
        
        self.rntexture = sdl2.SDL_CreateTextureFromSurface(self.rn, surfaceText)
        self.rectText = sdl2.SDL_Rect(self.x + (surfaceText.contents.w // 2), self.y + (surfaceText.contents.h // 2), surfaceText.contents.w, surfaceText.contents.h)

    def update(self, string):
        if self.inCharge:
            self.text += string
            self.renderText()

    def draw(self):
        sdl2.SDL_SetRenderDrawColor(self.rn, self.bg[0], self.bg[1], self.bg[2], self.bg[3])
        
        sdl2.SDL_RenderFillRect(self.rn, self.rect)
        sdl2.SDL_RenderCopy(self.rn, self.rntexture , None, self.rectText)

        sdl2.SDL_SetRenderDrawColor(self.rn, 0, 0, 0, 0)