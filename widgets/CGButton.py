class Button:
    def __init__(self, x, y, width, height, text, rn, command):
        self.showing = True

        self.x = x
        self.y = y 

        self.width = width
        self.height = height

        self.bg = [255, 255, 255, 255]
        self.fg = [0, 0, 0, 255]

        self.borderWidth = 5
        self.borderColor = [235, 64, 52, 255]

        self.fontSize = 16
        self.text = text

        self.rect = sdl2.SDL_Rect(self.x, self.y, self.width, self.height)

        self.status = True
        self.hovering = False
        self.rn = rn

        self.command = command

        self.renderText()

    def renderText(self):
        self.font = sdl2.sdlttf.TTF_OpenFont(str.encode("assets/fonts/font.ttf"), self.fontSize)
        surfaceText = sdl2.sdlttf.TTF_RenderText_Blended(self.font, str.encode(self.text), sdl2.SDL_Color(self.fg[0], self.fg[1], self.fg[2]))
        
        self.rntexture = sdl2.SDL_CreateTextureFromSurface(self.rn, surfaceText)
        self.rectText = sdl2.SDL_Rect(self.x + ((self.width - surfaceText.contents.w) // 2), self.y + ((self.height - surfaceText.contents.h) // 2), surfaceText.contents.w, surfaceText.contents.h)

    def draw(self):
        sdl2.SDL_SetRenderDrawColor(self.rn, self.bg[0], self.bg[1], self.bg[2], self.bg[3])
        
        sdl2.SDL_RenderFillRect(self.rn, self.rect)
        sdl2.SDL_RenderCopy(self.rn, self.rntexture , None, self.rectText)

        sdl2.SDL_SetRenderDrawColor(self.rn, self.borderColor[0], self.borderColor[1], self.borderColor[2], self.borderColor[3])

        for i in range(1, self.borderWidth + 1):
            rectBorder = sdl2.SDL_Rect(self.x - i, self.y - i, self.width + i * 2 , self.height + i * 2)

            sdl2.SDL_RenderDrawRect(self.rn, rectBorder)

        sdl2.SDL_SetRenderDrawColor(self.rn, 0, 0, 0, 0);
