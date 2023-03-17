import sys, os; sys.path.insert(1, os.path.join(sys.path[0], '..'))
from CGCore import *

app = CubicGUI()
app.createWin(100, 100, 1080, 720, 'Entry Test')

E1 = app.createEntry(500, 500, 200, 100, [255, 0, 0, 255])
E1.inCharge = True

while app.running:
    app.update()