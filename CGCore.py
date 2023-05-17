import sys
import ctypes
import sdl2
import sdl2.sdlttf

import widgets.CGWindow, widgets.CGButton, widgets.CGText, widgets.CGImage, widgets.CGEntry, widgets.CGShape, widgets.CGImgButton

class CubicGUI:
    def __init__(self):
        sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
        sdl2.sdlttf.TTF_Init()

        self.win = None
        self.s = sdl2.SDL_Renderer()

        self.buttons = []
        self.texts = []
        self.images = []
        self.entries = []

        self.shapes = []

        self.running = True
        
    def update(self):
        # Events  
        event = sdl2.SDL_Event()

        last_key = ''
        
        while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
            mouseX, mouseY = ctypes.c_int(0), ctypes.c_int(0) 
            mouse = sdl2.mouse.SDL_GetMouseState(ctypes.byref(mouseX), ctypes.byref(mouseY))
            mousePoint = sdl2.SDL_Point(mouseX, mouseY)

            sdl2.SDL_RenderClear(self.s)

            if event.type == sdl2.SDL_QUIT:
                sdl2.SDL_DestroyWindow(self.win.w)
                sdl2.SDL_Quit()

                self.running = False

            if event.type == sdl2.SDL_KEYDOWN:
                last_key = sdl2.SDL_GetKeyName(event.key.keysym.sym)
                last_key = last_key.decode("utf8")

                for entry in self.entries:
                    if entry.inCharge:
                        if len(last_key) == 1:
                            entry.update(last_key)

                        else:
                            if last_key == 'Space':
                                entry.update(' ')
                            
                            elif last_key == 'Backspace':
                                if len(entry.text) > 1:
                                    entry.text = entry.text[:len(entry.text)-1]
                                    entry.renderText()

                                if len(entry.text) == 1:
                                    entry.text = ' '
                                    entry.renderText()                            

            for entry in self.entries:
                if entry.showing:
                    entry.draw()

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

            for shape in self.shapes:
                if shape.showing:
                    shape.draw()

            sdl2.SDL_RenderPresent(self.s) 

    def createWin(self, x: int, y: int, width: int, height: int, title: str):
        """Creates a New Window"""

        self.win = widgets.CGWindow.Window(x, y, width, height, title)

        self.s = sdl2.SDL_CreateRenderer(self.win.w, -1, sdl2.SDL_RENDERER_ACCELERATED)

    def createButton(self, x: int, y: int, width: int, height: int, text: str, command=print):
        """Creates a Button"""

        b = widgets.CGButton.Button(x, y, width, height, text, self.s, command)
        self.buttons.append(b)

        return b

    def createImageButton(self, x: int, y: int, width: int, height: int, file: str, command=print):
        """Creates A Button with an Image"""

        ib = widgets.CGImgButton.ImgButton(x, y, width, height, file, self.s, command)
        self.buttons.append(ib)

        return ib

    def createText(self, x: int, y: int, text: str, color: list, fontsize: int):
        """Create a TextField"""

        t = widgets.CGText.Text(x, y, text, color, fontsize, self.s)
        self.texts.append(t)

        return t

    def createImage(self, x: int, y: int, width: int, heigth: int, file: str):
        """Create your Image with given width and height"""
        
        i = widgets.CGImage.Image(x, y, width, heigth, file, self.s)
        self.images.append(i)

        return i    

    def createEntry(self, x: int, y: int, width: int, height: int, color: list):
        """Create an Entry"""

        e = widgets.CGEntry.Entry(x, y, width, height, color, self.s)
        self.entries.append(e)

        return e

    def drawRectangle(self, x: int, y: int, width: int, height: int, color: list, Fillness: bool):
        """Draw a rectangle"""

        r = widgets.CGShape.Rectangle(x, y, width, height, color, Fillness, self.s)
        self.shapes.append(r)

        return r

    def drawRoundRectangle(self, x: int, y: int, width: int, height: int, radius: int, color: list, Fillness: bool):
        """Draw a round rectangle"""

        r = widgets.CGShape.RoundRectangle(x, y, width, height, radius, color, Fillness, self.s)
        self.shapes.append(r)

        return r

    def drawCircle(self, x: int, y: int, radius: int, color: list, Fillness: bool):
        """Draw a circle"""

        c = widgets.CGShape.Circle(x, y, radius, color, Fillness, self.s)
        self.shapes.append(c)

        return c 

    def drawEllipse(self, x: int, y: int, rx: int, ry: int, color: list, Fillness: bool):
        """Draw a ellipse"""

        e = widgets.CGShape.Ellipse(x, y, rx, ry, color, Fillness, self.s)
        self.shapes.append(e)

        return e

    def drawLine(self, x1: int, y1: int, x2: int, y2: int, color: list):
        """Draw a line"""

        l = widgets.CGShape.Line(x1, y1, x2, y2, color, self.s)
        self.shapes.append(l)

        return l    