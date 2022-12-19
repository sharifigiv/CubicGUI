from CGCore import * 

app = CubicGUI()
app.createWin(100, 100, 500, 500, 'TEST')

while app.running:
    app.update()

print('!')