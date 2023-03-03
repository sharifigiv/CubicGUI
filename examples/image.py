import sys, os; sys.path.insert(1, os.path.join(sys.path[0], '..'))
from CGCore import *

app = CubicGUI()

app.createWin(100, 100, 1080, 720, 'Image Test')

I1 = app.createImage(100, 100, 477 // 3, 477 // 3, 'assets/images/i.jpeg')
I2 = app.createImage(450, 100, 477 // 4, 477 // 4, 'assets/images/i.jpeg')
I3 = app.createImage(750, 100, 477 // 5, 477 // 2, 'assets/images/i.jpeg')

while app.running:
    app.update()