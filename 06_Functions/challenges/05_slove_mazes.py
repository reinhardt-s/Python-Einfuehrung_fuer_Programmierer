# Erstelle eine Funktion die mithilfe von Schleifen die Labyrinthe 1-5 selbstständig lösen kann

def solve_mazes():
    while not finished():
        turn_right()
        if not_facing_wall():
            move()
        else:
            turn_left()

        if not_facing_wall():
            move()
        else:
            turn_left()
            move()