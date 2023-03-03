import sys
import ctypes
import sdl2
import sdl2.sdlttf

import widgets.CGWindow, widgets.CGButton, widgets.CGText, widgets.CGImage, widgets.CGEntry

class CubicGUI:
    def __init__(self):
        sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
        sdl2.sdlttf.TTF_Init()

        self.win = None
        self.s = sdl2.SDL_Renderer()

        self.buttons = []
        self.texts = []
        self.images = []

        self.running = True
        
    def update(self):
        # Events  
        event = sdl2.SDL_Event()
        
        while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
            mouseX, mouseY = ctypes.c_int(0), ctypes.c_int(0) 
            mouse = sdl2.mouse.SDL_GetMouseState(ctypes.byref(mouseX), ctypes.byref(mouseY))
            mousePoint = sdl2.SDL_Point(mouseX, mouseY)

            sdl2.SDL_RenderClear(self.s)

            if event.type == sdl2.SDL_QUIT:
                sdl2.SDL_DestroyWindow(self.win.w)
                sdl2.SDL_Quit()

                self.running = False

            for text in self.texts:
                if text.showing:
                    text.draw()
             
            for button in self.buttons:
                if sdl2.SDL_PointInRect(mousePoint, button.rect) and button.showing:
                    if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
                        if button.status:
                            button.command()

                    else:
                        button.hovering = True
                else:
                    button.hovering = False

                if button.showing:
                    button.draw()

            for image in self.images:
                if image.showing:
                    image.draw()

            sdl2.SDL_RenderPresent(self.s) 

    def createWin(self, x, y, width, height, title):
        self.win = widgets.CGWindow.Window(x, y, width, height, title)

        self.s = sdl2.SDL_CreateRenderer(self.win.w, -1, sdl2.SDL_RENDERER_ACCELERATED)

    def createButton(self, x, y, width, height, text, command=print):
        b = widgets.CGButton.Button(x, y, width, height, text, self.s, command)
        self.buttons.append(b)

        return b

    def createText(self, x, y, text, color, fontsize):
        t = widgets.CGText.Text(x, y, text, color, fontsize, self.s)
        self.texts.append(t)

        return t

    def createImage(self, x, y, width, heigth, file):
        i = widgets.CGImage.Image(x, y, width, heigth, file)
        self.images.append(i)

        return i    