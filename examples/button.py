import sys, os; sys.path.insert(1, os.path.join(sys.path[0], '..'))
from CGCore import *

def testcommand():
    print("Clicked!")

app = CubicGUI()
app.createWin(100, 100, 1080, 720, 'TEST')

B = app.createButton(100, 100, 150, 500, 'ali', testcommand)
B1 = app.createButton(500, 100, 50, 50, 'gazaz')
B2 = app.createButton(700, 300, 50, 50, 'akhaz')

while app.running:
    if B.hovering:
        B.borderWidth = 20

    else:
        B.borderWidth = 0

    B2.showing = False
    app.update()