workout_plan = {
    "Montag": ["Clean and Press", "Kniebeuge", "Bergsteiger"],
    "Dienstag": ["Seilspringen", "Klimmzug", "Tauziehen"],
    "Mittwoch": {"Clean and Press": 5, "Kniebeuge": 15, "Bergsteiger": 30}
}


#Doppelbrot
my_set = {"Brot", "Käse", "Skyr", "Brot", "Kartoffeln"}

print(my_set)
# print(my_set[1])
# not allowed
#my_set[1] = "Gurke"
# print(my_set)

first_item = my_set.pop()
print(first_item)
print(my_set)

fridge = {"Käse", "Magerine", "Orange", "Skyr"}

frozen = frozenset(my_set)

print (fridge.intersection((my_set)))

print(workout_plan)
