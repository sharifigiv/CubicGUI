class Text:
    def __init__(self, x, y, text, color, fontsize, rn):
        self.x = x
        self.y = y

        self.text = text
        self.fontsize = fontsize

        self.fg = color

        self.rn = rn
        self.renderText()

    def renderText(self):
        self.font = sdl2.sdlttf.TTF_OpenFont(str.encode("assets/fonts/font.ttf"), self.fontSize)
        surfaceText = sdl2.sdlttf.TTF_RenderText_Blended(self.font, str.encode(self.text), sdl2.SDL_Color(self.fg[0], self.fg[1], self.fg[2]))
        
        self.rntexture = sdl2.SDL_CreateTextureFromSurface(self.rn, surfaceText)
        self.rectText = sdl2.SDL_Rect(self.x + ((self.width - surfaceText.contents.w) // 2), self.y + ((self.height - surfaceText.contents.h) // 2), surfaceText.contents.w, surfaceText.contents.h)

    def draw(self):
        pass    