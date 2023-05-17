import sys, os; sys.path.insert(1, os.path.join(sys.path[0], '..'))
from CGCore import *

app = CubicGUI()
app.createWin(100, 100, 1080, 720, 'Shape Test')

R1 = app.drawRectangle(100, 100, 200, 100, [255, 255, 255, 255], True)
R2 = app.drawRectangle(500, 500, 300, 150, [255, 0, 0, 255], False)
R3 = app.drawRoundRectangle(400, 150, 200, 150, 50, [235, 177, 30, 255], False)
R4 = app.drawRoundRectangle(650, 100, 150, 200, 25, [232, 232, 232, 255], True)

C1 = app.drawCircle(350, 500, 100, [30, 204, 235, 255], True)
E1 = app.drawEllipse(940, 170, 90, 60, [255, 0, 0, 255], True)

L1 = app.drawLine(0, 720 // 2, 1080, 720 // 2, [0, 255, 0, 255])

while app.running:
    app.update()