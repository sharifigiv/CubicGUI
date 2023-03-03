import sys, os; sys.path.insert(1, os.path.join(sys.path[0], '..'))
from CGCore import *

app = CubicGUI()
app.createWin(100, 100, 1080, 720, 'Shape Test')

R1 = app.drawRectangle(100, 100, 50, 20, [255, 255, 255, 255])

while app.running:
    app.update()