from CGCore import * 

def testcommand():
    print("Clicked!")

app = CubicGUI()
app.createWin(100, 100, 1080, 720, 'TEST')

B = app.createButton(100, 100, 150, 500, 'ali', testcommand)
B1 = app.createButton(500, 100, 50, 50, 'gazaz')
B2 = app.createButton(700, 300, 50, 50, 'akhaz')

T1 = app.createText(100, 100, 'Mayam Bash!', [255, 255, 255, 255], 32)

I1 = app.createImage(100, 100, 477 // 2, 477 // 2, 'assets/images/i.jpeg')
I2 = app.createImage(100, 400, 477 // 3, 477 // 3, 'assets/images/i.jpeg')

while app.running:
    if B.hovering:
        B.borderWidth = 20

    else:
        B.borderWidth = 0

    B2.showing = False
    B1.showing = False
    B.showing = False

    app.update()

print('!')
