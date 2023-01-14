from CGCore import * 

app = CubicGUI()
app.createWin(100, 100, 1080, 720, 'TEST')

B = app.createButton(100, 100, 150, 500, 'ali')
B.radius = 20

while app.running:
    app.update()
    B.show()

    B.fontSize = 16
    B.borderWidth = 12

print('!')
