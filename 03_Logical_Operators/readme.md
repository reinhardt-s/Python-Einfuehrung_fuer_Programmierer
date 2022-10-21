## Themen 

* if/else
* Conditional Operators

## Was wir programmieren
* Ein Textadventure "Baboon Island" !
* Einen Kaffeeautomaten
* Schaltjahrermittler


## Ablauf
* if / else
  * Vergleich mit roter Ampel
* Conditionals / Bedingungen 
  * ```
    Wenn Ampel grün:
        Weiterfahren
    Sonst:
        Bremsen
    ```
  * ```python
    if condition:
      do this
    else:
      do that
    ```
  * Wird ausgeführt wenn, Bedingung wahr `True` ist 
  * Einrückung beachten!
    * if else stehen als paar auf gleicher ebene
    * unter if und else eingerückte gehören zur jeweiligen auswertung der bedingung
    * condition ergibt immer `True` oder `False`
* Beispiel Ticketverkauf
* Operatoren
  *  | Operator | Bedeutung      |
     ----------|----------------
     | `<`      | Kleiner        |
     | `>`      | Größer         |
     | `==`| Gleich         |
     | `!=`| Ungleich       |
     | `<=`     | Kleiner-Gleich |
     | `>=`     | Größer-Gleich  |

* Kaffeeautomat challenge
  * Flowchart
* Modulo Operator
  * %
  * Gibt an, ob eine Division einen Rest hat oder nicht
  * `print(9%2)`
  * Gerade Zahlen können restlos durch 2 geteilt werden
  * challenge 02_even_modulo
* nested if
  * werden nacheinander abgearbeitet sofern die obere Bedingung wahr ist
* wie werden if auf gleicher Ebene Abgehandelt?
* elif
  * challenge 03_coffee
    * Flowchart
* Challenge 04_leapyear
* Challenge 05_pizza_order
* Logical Operators
  * `and` - Verknüpft Bedingungen
    * ```python
        if pizza_size == "M" and extra_cheese == "J":
          cost = cost_m + cost_cheese
        else
            ...
      ```
  * `or` Oder Bedingung
    * ```python
      if add_pepperoni == "Y":
        if pizza_size == "M" or pizza_size == "L":
          cost += 3
      ```
  * `not` Negierende Bedingung
    * ```python
      if add_pepperoni == "Y":
        if not pizza_size == "S":
          cost += 3
      ```