## Themen 
* Listen
* Zufallszahlen


## Was wir programmieren
Pay Roulette 
Stein - Schere - Papier - Echse - Spock

## Ablauf
* Zufallswerte
  * Im Spiel für Unvorhersehbarkeit
  * Zum Generieren von Beispieldaten
  * Computer sind deterministisch
    * Es gibt also keinen echten Zufall
    * Es gibt verschiedene Methoden Pseudozufallszahlen zu generieren
    * Python nutzt Mersenne Twister -> wiki
    * Wollen das Rad nicht neu erfinden. python got your back
    * AskPython aufrufen
  * Erklärung das random ein Modul ist
    * ist sinnvoll aufgaben aufzuteilen
    * wir können eigene module erstellen
    * `random.random()` ist zwischen 0-1
      * wie zwische 0 und 5?
* Listen
  * Liste  ist eine Datenstruktur
    * eine Möglichkeit daten zu organisieren und zu speichern
    * zusammenhängende daten in einer datenstruktur speichern
    * liste ist auch reihenfolge
    * gekennzeichnet durch ekige klammer
    * kann alles datentypen beinhalten. auch gemischt
    * bestimmte position mit `[]` angeben
    * fangen bei 0 an zu zählen
      * `len()` funktioniert aus bei Listen 
      * bildlich: wie weit muss ich den cursor verschieben?
      *  -1, -2 etc beginnt hinten zu zählen!
      * anfügen von elementen `.append()`
      * Dokumentation hilft
    * `str.split()`
* Pay Roulette
  * erklären, was es ist
  * Challenge 02 Pay Roulette
  * `random.choice()`
* IndexErrors
  * list index out of range
* Nested Lists
  * https://www.ewg.org/foodnews/summary.php
  * Liste mit belasteten Obst und Gemüse
  * Zugriff auf Element in Nested List
  * quiz 03
  * challenge 04 baboon figure
* Challenge 05 RPSLS
