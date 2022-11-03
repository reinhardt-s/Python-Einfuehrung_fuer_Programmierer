import random
import my_module

random_int = random.randint(1, 10)
print(random_int)
# 0.000000 - 0.999999
print(random.random()*5)

print(my_module.pi)
#############################
#lists

var1 = 1
var2 = "5"
customer_queue = ["Guybrush Threepwood", "LeChuck", "Elaine Marley", "Stan S. Stanman", "Murray"]
print(customer_queue)
results = [5, 3, random.randint(1, 9), 11]
print(results)
assembly_belt = [2, "Zahnrad", 5, "Muffe", False]

print(customer_queue[-2])
print(customer_queue[1])
customer_queue[1] = "Geisterpirat"
print(customer_queue[1])
customer_queue.append("Herman Toothrot")
print(customer_queue)
customer_queue.extend(["Frank Drebbin", "Stan Marsh"])
print(customer_queue)
customer_count = len(customer_queue)
print(f"Es befinden sich {customer_count} Kunden in der Warteschlange")

recipe = "500g Mehl, 117g Salz, Löffel Butter, 250ml Wasser, 3 Eier"
recipe_list = recipe.split(", ")
print(recipe_list)

# index error
# print(customer_queue[40])


# nested lists
# dirty_dozen = ["Strawberries", "Spinach", "Kale collard and mustard greens",
#                "Nectarines", "Apples", "Grapes", "Bell and hot peppers",
#                "Cherries", "Peaches", "Pears", "Celery", "Tomatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes",
          "Cherries", "Peaches", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[0][1])


