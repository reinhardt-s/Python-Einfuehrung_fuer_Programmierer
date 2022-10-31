# Bei der Krusty Krab wurde endlich ein Drive Through eröffnet
# Unsere App soll die eingegangenen Bestellungen in Arbeitsstationen aufteilen
# Station 1: Wärmt Buns auf -> "warm buns"
# Station 2: Brät Patties -> "grilled patty"
# Station 3: Mixt Plankton in Sea Foam -> "sea foam soda"
# Station 4: Rollt ein Krabby Meal aus Salmon, Wasabi, Nori und geschnittener Sea Cucumber -> krabby meal
# Station 5: Schneidet Sea Cucumber -> "cuttet sea cucumber"
# Station 6: Kombiniert aufgewärmte warm buns, cheese, (2)grilled patties, cuttet sea cucumber
#            und ketchup zu (double)krabby patty
# Nachdem Zutaten in einer Station bearbeitet wurden, werden, die Rohzutaten aus der Rezeptzutatenliste gelöscht
# und die fertige Zutat, bzw. das fertige gericht stattdessen eingefügt.
# Gib bei jeder Arbeitsstation aus, welche Zutat gerade zu was verarbeitet wird.


krabby_patty = ["patty", "bun", "sea cucumber", "ketchup", "cheese"]
double_krabby_patty = ["patty", "patty", "bun", "sea cucumber", "ketchup", "cheese"]
krabby_meal = ["salmon", "wasabi", "nori", "sea cucumber"]
sea_foam_soda = ["sea foam", "plankton"]

order_1 = [krabby_patty, krabby_meal, sea_foam_soda, sea_foam_soda]
order_2 = [double_krabby_patty, sea_foam_soda, krabby_meal]

# Bestellungen kombinieren
orders = [order_1, order_2]

for order in orders:
    for meal in order:
        for ingredient in meal:
            if ingredient == "bun":
                print("Station 1: Wäre Bun auf")

