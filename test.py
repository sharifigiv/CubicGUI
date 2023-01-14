from CGCore import * 

def testcommand():
    print("Clicked!")

app = CubicGUI()
app.createWin(100, 100, 1080, 720, 'TEST')

B = app.createButton(100, 100, 150, 500, 'ali', testcommand)
B.radius = 20

while app.running:

    app.update()
    if B.hovering:
        B.borderWidth = 20

    else:
        B.borderWidth = 0

    B.show()

print('!')
