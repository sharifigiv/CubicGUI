from CGCore import * 

app = CubicGUI()
app.createWin(100, 100, 500, 500, 'TEST')

while True:
    app.update()
    app.win.show()