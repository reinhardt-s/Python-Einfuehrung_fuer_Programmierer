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
