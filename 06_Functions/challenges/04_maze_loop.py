# Laufe im Zick-Zack den Sandkasten ab, bis du beim Schatz bist
# Dir stehen dafür not_facing_wall und finished zur Verfügung
# Versuche die Aufgabe mit while loops zu lösen

def playground_loop():
    # it 3
    going_up = True

    # it 2
    while not finished():
        # it 1
        while not_facing_wall():
            move()
        if going_up:
            turn_right()
            move()
            turn_right()
            going_up = False
        else:
            turn_left()
            move()
            turn_left()
            going_up = True