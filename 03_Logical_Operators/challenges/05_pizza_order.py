# Schreibe ein Programm welches, den Preis der bestellten Pizza ermittelt
# Kosten:
# Pizza S = 3,50 €
# Pizza m = 5,50 €
# Pizza L = 7,00 €
# Pepperoni auf Pizza S = 2 €
# Pepperoni auf Pizza M, L = 3 €
# Extra Käse auf allen Pizzen = 1 €

print("Willkommen bei Pauls Pizza Palast!")
size = input("Wie groß soll deine Pizza sein? S,M oder L \n")
add_peperoni = input("Möchtest du Peperoni dazu? J,N \n")
extra_cheese = input("Möchtest du extra Käse dazu? J,N\n")
# Dein Code nach dieser Zeile

cost = 0
if size == "S":
    cost += 3.5
    if add_peperoni == "J":
        cost += 2
elif size == "M":
    cost += 5.5
    if add_peperoni == "J":
        cost += 3
else:
    cost += 7
    if add_peperoni == "J":
        cost += 3

if extra_cheese == "J":
    cost += 1

cost = "{:.2f}".format(cost)

print(f"Deine Pizza kostet {cost} €")
