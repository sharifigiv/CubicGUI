import sys
import ctypes
import sdl2
import sdl2.sdlttf

class CubicGUI:
    def __init__(self):
        sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
        sdl2.sdlttf.TTF_Init()

        self.win = None
        self.s = sdl2.SDL_Renderer()

        self.buttons = []

        self.running = True
        
    def update(self):
        # Events  
        event = sdl2.SDL_Event()

        while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == sdl2.SDL_QUIT:
                sdl2.SDL_DestroyWindow(self.win.w)
                sdl2.SDL_Quit()

                self.running = False

    def createWin(self, x, y, width, height, title):
        self.win = Window(x, y, width, height, title)

        self.s = sdl2.SDL_CreateRenderer(self.win.w, -1, sdl2.SDL_RENDERER_ACCELERATED)

    def createButton(self, x, y, width, height, text):
        b = Button(x, y, width, height, text, self.s)

        self.buttons.append(b)

        return b

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

class Button:
    def __init__(self, x, y, width, height, text, rn):
        self.x = x
        self.y = y 

        self.width = width
        self.height = height

        self.bg = [255, 255, 255, 255]
        self.fg = [0, 0, 0, 255]

        self.borderWidth = 5
        self.borderColor = [235, 64, 52, 255]

        self.status = True
        self.rn = rn

        self.rect = sdl2.SDL_Rect(self.x, self.y, self.width, self.height)

        self.fontSize = 16
        self.text = text

        self.renderText()

    def renderText(self):
        self.font = sdl2.sdlttf.TTF_OpenFont(str.encode("assets/fonts/font.ttf"), self.fontSize)
        surfaceText = sdl2.sdlttf.TTF_RenderText_Blended(self.font, str.encode(self.text), sdl2.SDL_Color(self.fg[0], self.fg[1], self.fg[2]))
        
        self.rntexture = sdl2.SDL_CreateTextureFromSurface(self.rn, surfaceText)
        self.rectText = sdl2.SDL_Rect(self.x + ((self.width - surfaceText.contents.w) // 2), self.y + ((self.height - surfaceText.contents.h) // 2), surfaceText.contents.w, surfaceText.contents.h)

    def show(self):
        sdl2.SDL_RenderClear(self.rn)
        sdl2.SDL_SetRenderDrawColor(self.rn, self.bg[0], self.bg[1], self.bg[2], self.bg[3])
        
        sdl2.SDL_RenderFillRect(self.rn, self.rect)
        sdl2.SDL_RenderCopy(self.rn, self.rntexture , None, self.rectText)

        sdl2.SDL_SetRenderDrawColor(self.rn, self.borderColor[0], self.borderColor[1], self.borderColor[2], self.borderColor[3])

        for i in range(1, self.borderWidth + 1):
            rectBorder = sdl2.SDL_Rect(self.x - i, self.y - i, self.width + i * 2 , self.height + i * 2)

            sdl2.SDL_RenderDrawRect(self.rn, rectBorder)

        sdl2.SDL_SetRenderDrawColor(self.rn, 0, 0, 0, 0);
        sdl2.SDL_RenderPresent(self.rn)    
