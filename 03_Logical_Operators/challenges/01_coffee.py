# Erstelle einen Kaffeeautomaten welches aufhört die Tasse zu befüllen, wenn der Tassenfüllstand
# die maximale Füllmenge erreicht hat. Gebe dann "Der Kaffee ist fertig" aus. Gebe andernfalls "Fülle auf..." aus
# Dieses Programm werden wir sukzessiv in verschiedenen Challenges erweitern

max_in_ml = 150
filled_to_in_ml = int(input("Wie viel ML Kaffee sind in der Tasse?\n"))  # Tassenfüllstand

if filled_to_in_ml >= max_in_ml:
    print("Der Kaffee ist fertig.")
else:
    print("Fülle auf")
