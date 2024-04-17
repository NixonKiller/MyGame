gameStarted = False
degree_lines = [(0, "0"), (45, "45"), (90, "90"), (135, "135"), (180, "180"), (225, "225"), (270, "270"), (315, "315")]
from random import choice

# Variable to store the current angle the player needs to guess
current_angle = None

def setup():
    size(400, 400)
    background(255)  # Change background color to white
    textSize(32)
    textAlign(CENTER, CENTER)
    fill(0)
    text("Welcome to RadPi", width/2, 150)
    textSize(23)
    text("Click 'K' on your keyboard to start the game!", width/2, 230)

def draw():
    global gameStarted
    global current_angle
    
    if gameStarted:
        background(300, 40, 190)  # Placeholder background for the game
        noFill()
        ellipse(width/2, height/2, 300, 300)
        fill(255)
        stroke(100)
        line(40, 363, 325, 70)  # 45
        line(30, 200, 370, height/2)  # x axis
        line(200, 370, 200, 30)  # y axis
        line(40, 40, 325, 325)  # 45
        line(30, 131, 350, 262)  # 160
        line(135, 33, 260, 350)  # 120
        line(30, 275, 350, 135)  # 30
        line(140, 350, 255, 60)  # 60
        
        # Highlight a random angle for the player to guess
        if current_angle is None:
            current_angle = choice(degree_lines)[0]
            print("Guess the angle: ", current_angle)

def keyPressed():
    global gameStarted
    global current_angle
    if not gameStarted and key == 'k':
        gameStarted = True
    elif gameStarted and key.isdigit():
        if current_angle is not None:
            # If previous key pressed was also a digit, concatenate them to form a double-digit guess
            if 'lastKey' in globals() and lastKey.isdigit():
                guess = int(str(lastKey) + key)
                check_guess(guess)
            else:
                # If previous key pressed was not a digit, store the current key as last key
                globals()['lastKey'] = key

def check_guess(guess):
    global current_angle
    if guess == current_angle:
        print("Correct!")
        current_angle = None
    else:
        print("Incorrect!")
