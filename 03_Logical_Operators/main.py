# # Ticketverkauf
# # Kinder bekommen ermäßigten Eintritt
#
# child_till_age = 12 # Maximales Alter für Rabatt
# discount = 0.25  # 25 % Rabatt für Kinder
# cost = 15  # Kosten pro Ticket
#
# # Alter der Kund*in
# age = int(input("Wie alt bist du?\n"))
#
#
# if age <= child_till_age:
#     with_discount = cost * (1-discount)
#     with_discount = "{:.2f}".format(with_discount)
#     print(f"Dein Ticket kostet {with_discount}")
# else:
#     print(f"Dein Ticket kostet {cost}")
#
#
# print(9%2)
# 2+2+2+2+1
#
# val2 = 10
# val1 = 15
# if (val2 > 5 and val2 < 10) or (val1 < 10 or val2 > 5):
#     print(True)


# import random
#
# bag = []
# for _ in range(85):
#     bear_type = random.randint(0,6)
#
#     if bear_type == 0:
#         bag.append("w")
#     elif bear_type == 1:
#         bag.append("y")
#     elif bear_type == 2:
#         bag.append("g")
#     elif bear_type == 3:
#         bag.append("r")
#     elif bear_type == 4:
#         bag.append("o")
#     elif bear_type == 5:
#         bag.append("p")
#
#     if random.randint(0,1) == 1:
#         bag[len(bag)-1] = str(bag[len(bag)-1]).upper()
#
# print(bag)
