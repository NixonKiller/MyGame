gameStarted = False

def setup():
    size(400, 400)
    background(500)
    textSize(32)
    textAlign(CENTER, CENTER)
    fill(0)
    text("Welcome to RadPi", width/2,150)
    textSize(23)
    text("Click K on your keyboard to start the game!", width/2, 230)
    #photo = loadImage("pi.png")
def draw():
    global gameStarted
    if gameStarted:
        background(300,40,190)  # Placeholder background for the game
        fill(90)
        createShape(ELLIPSE,0,0,100,100)

def keyPressed():
    global gameStarted
    if not gameStarted and key == 'k':
        gameStarted = True
        # Here you can add code to initialize and start the game
