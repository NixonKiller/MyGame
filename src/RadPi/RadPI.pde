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
        noFill
        ellipse(width/2, height/2, 300, 300) 
        fill(255)
        stroke(100)
        line(width/2,height/2,1,0)
        line(width/2,height/2,0,-1)
        
        strokeWeight(2)
        line(200,200,200,200)
    global gameStarted
    if not gameStarted and key == 'k':
        gameStarted = True
        # Here you can add code to initialize and start the game
