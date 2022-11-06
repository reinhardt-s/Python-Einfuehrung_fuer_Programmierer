# Schreibe einer Funktion order_food(order) welche folgende Anforderungen erfüllt:
# * order ist die Liste mit bestellten Essen
# * beim ersten Aufruf von order_food wird die Kund*in gefragt: "Was darf's denn sein?",
# * be jedem weiteren "Und dann?"
# * das Essen wird der order-Liste hinzugefügt
# * wenn die Kund*in nicht mit "kein und dann" antwortet, ruft die Funktion sich rekursiv erneut auf,
#   um weitere Bestellpositionen aufzunehmen

# Dein Code nach dieser Zeile


def order_food(order):
    if len(order) == 0:
        order.append(input("Was darf's denn sein?\n"))
    else:
        order.append(input("Und dann?\n"))

    if order[-1] == "kein und dann":
        order.remove("kein und dann")
        print("Danke für Ihre Bestellung.")
        return order

    return order_food(order)


# Dein Code über dieser Zeile


print("Sie haben bestellt:")
for item in order_food([]):
    print(item)
