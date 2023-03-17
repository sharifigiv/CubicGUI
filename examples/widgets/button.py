import sys, os; sys.path.insert(1, os.path.join(sys.path[0], '..'))
from CGCore import *

def testcommand():
    print("Clicked!")

app = CubicGUI()
app.createWin(100, 100, 1080, 720, 'Button Test')

B = app.createButton(100, 100, 150, 500, 'ali', testcommand)
B1 = app.createButton(500, 100, 50, 50, 'gazaz')
B2 = app.createButton(700, 300, 150, 150, 'akhaz')

while app.running:
    if B1.hovering:
        B1.borderWidth = 5

    else:
        B1.borderWidth = 0

    B.showing = False
    app.update()