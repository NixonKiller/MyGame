boolean gameStarted = false;
void setup() {
  size(400, 400);
  background(255);
  textSize(40);
  textAlign(CENTER, CENTER);
  fill(22);
  text("Welcome to RadPi", width/2, 150);
  textSize(23);
  text("Click K on your keyboard to start playing!", width/2,250);
}
void draw() {
  if (gameStarted) {
    background(200); // Placeholder background for the game
  }
}

void keyPressed() {
  if (!gameStarted && (key == 'k' || key == 'K')) {
    gameStarted = true;
    // Here you can add code to initialize and start the game
  }
}
