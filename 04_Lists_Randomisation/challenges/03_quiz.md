
## Frage 1

---
```python
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
```
Welche der Optionen gibt `"Apples"` zurück? 

* `fruits[3]`
* `fruits[4]`
* `fruits.Apples`
* `fruits[-5]`
* `fruits[-3]`

## Frage 2

----
```python
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)
```
Was wird ausgegeben?  
* `["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Melons", "Lemons"]`
* `["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Melons", "Lemons"]`
* `["Melons", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Lemons]`

## Frage 3

----
```python
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])
```

Was wird ausgegeben?

* `"Kale"`
* `"Nectarine"`
* `["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]`
* `"Celery"`