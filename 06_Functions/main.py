<<<<<<< HEAD
# ingredients = ["Teig", "Tomatensauce", "Käse", "Salami", "Sardinen"]
# amounts = ["125g", "200ml", "600g", "110g", "1l"]
# instruction = [ingredients, amounts]
#
# for ingredient in ingredients:
#     print(ingredient)
#
#
# for item in instruction:
#     for sub_item in item:
#         print(sub_item)
#
# # using range
# for number in range(1, 11, 3):
#     print(number)

# def -> hier definiere ich eine function
# my_function -> name der funktion
# () -> parentheses -> hier drin könne argumente stehen
# : ende des functionsdefinitionskopfes
# ab kommender zeile folgt eingerückt (indented), der körper der funktion

def my_function():
    print("my_function aufgerufen")

# die function muss aufgerufen werden, klingt logisch oder?
# aufruf erfolgt durch schreiben der functionsnamen und der benötigten argumente
# da unsere function keine benötigt, bleibt die klammer leer

# blueprint, wie eine funktion ausieht

# was passiert, wenn ich den aufruf von my_function mache, bevor ich die function definiert habe?
# NameError: name 'my_function' is not defined
my_function()
my_function()
=======
ingredients = ["Teig", "Tomatensauce", "Käse", "Salami", "Sardinen"]
amounts = ["125g", "200ml", "600g", "110g", "1l"]
instruction = [ingredients, amounts]

for ingredient in ingredients:
    print(ingredient)


for item in instruction:
    for sub_item in item:
        print(sub_item)

# using range
for number in range(1, 11, 3):
    print(number)
>>>>>>> origin/master
