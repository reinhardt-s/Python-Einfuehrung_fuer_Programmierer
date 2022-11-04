# Schreibe eine App, welche mit den Parametern: distance, cost_per_liter, liter_per_100_km,
# Task 1 - Erstelle eine Funktion ask_user_for_data, in welche die Nutzer*in nach den drei Werten fragt
# Task 2 - Erstelle eine Funktion calc_cost, welche diese drei Werte annimmt
# Task 3 - Berechnung und Ausgabe der Kosten.
# Task 4 - Rufe aus ask_user_for_data die Funktion calc_cost auf und rufe ask_user_for_data selbst auf

def ask_user_for_data():
    trip_distance = int(input("Wie lang ist die Route in Kilometern?\n"))
    cost_per_liter = float(input("Wie viel kostet ein Liter Benzin?\n"))
    liter_per_100_km = float(input("Wie viel Benzin benötigt das Fahrzeug durchschnittlich für 100km?\n"))
    calc_cost(trip_distance, cost_per_liter, liter_per_100_km)


def calc_cost(distance, cost, consumption):
    consumption_per_km = consumption/100
    result = distance*cost*consumption_per_km
    result = "{:.2f}".format(result)
    print(f"Die Fahrt wird in etwa {result} € kosten.")


ask_user_for_data()



