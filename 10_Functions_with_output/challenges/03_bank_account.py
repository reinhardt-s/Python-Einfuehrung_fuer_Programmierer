# Schreibe ein Programm, welches folgende Funktionen erfüllt:
# * Anzeigen der Kontoübersicht mit get_overview()
#   * Je Zeile steht Links die Beschreibung und rechts der Betrag
#     Netflix                                 -14.20 €
# * Ausgabe des aktuellen Kontostandes mit get_balance()
# * new_entry(transaction_type, amount, description) erzeugt Dictionary
#   * Mit z.B. account.append(new_entry("Abbuchung", 14.20, "Netflix")) kann dieser der Liste account hinzugefügt werden

account = []

# Dein Code unter dieser Zeile

def new_entry(transaction_type, amount, description):
    entry = {
        "transaction_type": transaction_type,
        "amount": amount,
        "description": description
    }
    return entry


def get_balance():
    balance = 0
    for entry in account:
        if entry["transaction_type"] == "Einzahlung":
            balance += entry["amount"]
        elif entry["transaction_type"] == "Abbuchung":
            balance -= entry["amount"]
    return "{:.2f}".format(balance)


def get_overview():
    output = ""
    for entry in account:
        amount = entry["amount"]
        if entry["transaction_type"] == "Abbuchung":
            amount *= -1

        amount = "{:.2f}".format(amount)
        output += f"{entry['description']} {amount.rjust(37-len(entry['description']),' ')} €\n"
    output += "="*40
    return output

# Dein Code über dieser Zeile


account.append(new_entry("Abbuchung", 14.20, "Netflix"))
account.append(new_entry("Einzahlung", 3244.60, "Lohn Juni"))
account.append(new_entry("Abbuchung", 35.77, "Amazon"))
account.append(new_entry("Abbuchung", 97.60, "Amazon"))
account.append(new_entry("Abbuchung", 260.26, "Hotel Waschbär"))
account.append(new_entry("Abbuchung", 870.40, "Miete"))
account.append(new_entry("Abbuchung", 460.14, "Leasing"))

print(get_overview())
print("Kontostand:" + f"{get_balance()} €".rjust(29))




