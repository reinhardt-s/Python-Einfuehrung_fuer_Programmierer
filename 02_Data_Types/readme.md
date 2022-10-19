## Themen 

* Data Types
* Numbers
* Operations
* Type Conversions
* f-Strings

## Was wir programmieren
BMI-Rechner
Mehrwertsteuer-Rechner

## Ablauf
* `print(len(1234))` - error
  * Type Conversion
* Wir lernen `String, Integer, Float` und `Boolean` kennen
* Spaß mit `String`
  * Wir zählen immer von 0 an
  * Wir lernen, dass Strings nicht addieren, sondern konkatieren
* Spaß mit `Integer`
  * Integer lassen sich mit + addieren
  * Underscores dienen als Trennzeichen
* Spaß mit `Float`
  * Sind Kommazahlen
* Spaß mit `Boolean`
  * Kennt nur `True` und `False`
* `type()` gibt den Datentyp einer Variable an
* Type Conversion
  * mit `str` konvertieren wir zu String
  * mit `int` und `float` konvertieren
    * Konvertieren von float nach in schneidet Nachkommastellen ab
  * Praktische Übung `02_datatypes.py`
* Mathematische Operatoren
  * +, -, *, /, **
  * Divisionen ergeben immer ein float
  * Abarbeitungsreihenfolge in gleicher Codezeile
    * ()
    * \**
    * /, //
      * *// ergibt direkt ein int statt float
    * \+ \-
    * ltr
  * Runden von Zahlen
    * `round()`
      * Angabe der Nachkommastellen
  * += -= etc
  * f-Strings