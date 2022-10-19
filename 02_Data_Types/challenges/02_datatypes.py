# Geben Sie auf der Konsole die Quersumme des Wertes von number aus.
# Beispiel für number = 39 >> 3 + 9 = 12 <<
# Sie müssen dazu die beiden Ziffern von number zerlegen und addieren

number = input("Geben Sie eine zweistellige Zahl ein: ")
print(str(number)[0] + " + " + str(number)[1] + " = " + str(int(str(number)[0]) + int(str(number)[1])) )

# Hinweise
# Sie können, zur besseren Übersicht, Variablen anlegen.
# Überlegen Sie welchen Datentyp number hat
# Überlegen Sie, wie Sie die erste und letzte Stelle von number auslesen können
# Überlegen Sie wie sie die ausgelesenen Stellen addieren können
# Behalten Sie immer im Hinterkopf, welchen Datentyp Sie gerade verarbeiten
# Mit type() können Sie immer den Datentyp prüfen
