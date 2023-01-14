from CGCore import * 

app = CubicGUI()
app.createWin(100, 100, 1080, 720, 'TEST')

B = app.createButton(10, 10, 150, 500, 'ali')

while app.running:
    app.update()
    B.show()

    B.fontSize = 24

print('!')
