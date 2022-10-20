# Erweitere das Programm so, das je nach gewählter Kaffee-Zubereitung eine andere Füllmenge gewählt wird:
#   - (1) Kaffee       = 140 ml
#   - (2) Espresso     =  20 ml
#   - (3) Americano    = 450 ml
#   - (x) Alle anderen = 200 ml
# Erweitere das Kaffeeprogramm so, dass nach dem die Tasse gefüllt wurde,
# Milch hinzugegeben wird, so dies vom Kunden gewünscht ist.

max_in_ml = 1000  # Maximale Kaffeefüllmenge - kann überschrieben werden
# Kaffeesorte, angegeben durch 1,2 oder 3
coffee_type = int(input("Wählen Sie:\n1 - Kaffee\n2 - Espresso\n3 - Americano\n4 - Crema\n5 - Cold Brew\n"))
add_milk = input("Soll Milch hinzugefügt werden? (j/n)\n")  # wird zum Boolean
filled_to_in_ml = int(input("Wie viel ML Kaffee sind in der Tasse?\n"))  # Tassenfüllstand

if add_milk == "j":
    add_milk = True
else:
    add_milk = False

# Dein Code kommt unter dieser Zeile

if coffee_type == 1:
    max_in_ml = 140
elif coffee_type == 2:
    max_in_ml = 20
elif coffee_type == 3:
    max_in_ml = 450
else:
    max_in_ml = 200

if filled_to_in_ml >= max_in_ml:
    if add_milk:
        print("Füge Milch hinzu")
    print("Der Kaffee ist fertig.")
else:
    print("Fülle auf")
