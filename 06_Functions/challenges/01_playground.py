#Erstelle eine turn_left-Funktion
#   * Erstelle eine Funktion `playground()` welche du aus `solve_maze()` aufrufst
#     * Zeichne ein Quadrat mit einer Kantenlänge von vier Feldern auf den Spielplatz

def turn_left():
    turn_right()
    turn_right()
    turn_right()

def playground():
    turn_right()
    move()
    move()
    move()
    turn_left()
    move()
    move()
    move()
    turn_left()
    move()
    move()
    move()
    turn_left()
    move()
    move()
    move()