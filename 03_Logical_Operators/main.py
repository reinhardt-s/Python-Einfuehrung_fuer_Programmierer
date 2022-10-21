# Ticketverkauf
# Kinder bekommen ermäßigten Eintritt

child_till_age = 12 # Maximales Alter für Rabatt
discount = 0.25  # 25 % Rabatt für Kinder
cost = 15  # Kosten pro Ticket

# Alter der Kund*in
age = int(input("Wie alt bist du?\n"))


if age <= child_till_age:
    with_discount = cost * (1-discount)
    with_discount = "{:.2f}".format(with_discount)
    print(f"Dein Ticket kostet {with_discount}")
else:
    print(f"Dein Ticket kostet {cost}")


print(9%2)
2+2+2+2+1

val2 = 10
val1 = 15
if (val2 > 5 and val2 < 10) or (val1 < 10 or val2 > 5):
    print(True)
