from CGCore import * 

app = CubicGUI()
app.createWin(100, 100, 500, 500, 'TEST')

B = app.createButton(100, 300, 50, 100)

while app.running:
    app.update()
    B.show()

print('!')