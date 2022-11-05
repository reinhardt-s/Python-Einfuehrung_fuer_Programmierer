# Schreibe ein Programm, welches zu allen in der Liste food_advisor befindlichen Restaurants eine Bewertung ausgibt.
# Zur Bewertung des Restaurant wird folgende Formel angewandt:
# 100 / (upvotes + downvotes) * upvotes
# Runde das Ergebnis, ohne Nachkommastellen
# Füge die Funktion add_restaurant dem Programm hinzu

food_advisor = [
    {
        "restaurant": "El Erni",
        "upvotes": 250,
        "downvotes": 12
    },
    {
        "restaurant": "Duck Dich",
        "upvotes": 41,
        "downvotes": 33
    },
    {
        "restaurant": "Raffaello",
        "upvotes": 400,
        "downvotes": 13
    },
]

add_restaurant(restaurant="Reblaus", upvotes=670, downvotes=14)

for restaurant in food_advisor:
    rating = 100 / (restaurant["upvotes"] + restaurant["downvotes"]) * restaurant["upvotes"]
    print(f"{restaurant['restaurant']}: {round(rating)}%")
