import sys, os; sys.path.insert(1, os.path.join(sys.path[0], '..'))
from CGCore import *

app = CubicGUI()
app.createWin(100, 100, 1080, 720, 'Text Test')

T1 = app.createText(100, 100, "Mayam Bash", [0, 0, 255, 255], 32)
T2 = app.createText(200, 300, "Ali Bash!", [255, 255, 255, 255], 54)
T3 = app.createText(1080 // 2, 720 // 2, "Miumen", [0, 255, 0, 255], 16)

while app.running:
    app.update()