# Schreiben Sie ein Programm welche die Rechnung eines Tisches gleichmäßig auf alle Gäste aufteilt.
# Geben Sie das Ergebnis auf zwei Nachkommastellen gerundet aus.
# Berechnen Sie dann die Höhe des Trinkgeldes und geben Sie dann
#   - den Gesamtbetrag pro Gast
#   - den Rechnungsanteil ohne Trinkgeld pro Gast
#   - das Trinkgeld pro Gast
#   - das Gesamt-Trinkgeld
# in einer print()-Anweisung aus.

bill = float(input("Wie hoch ist die Rechnung?\n"))
customer_count = float(input("Durch wie viele Personen soll die Rechnung geteilt werden?\n"))
tip = float(input("Wie hoch soll das Trinkgeld ausfallen? (5%, 12%, 25%, ...)\n"))

bill_slice = round(bill / customer_count, 2)
tip_per_customer_in_eur = round(bill_slice * (tip/100), 2)
tip_total = round(tip_per_customer_in_eur * customer_count, 2)
bill_per_customer = bill_slice + tip_per_customer_in_eur

bill_slice = "{:.2f}".format(bill_slice)
tip_total = "{:.2f}".format(tip_total)
tip_per_customer_in_eur = "{:.2f}".format(tip_per_customer_in_eur)
bill_per_customer = "{:.2f}".format(bill_per_customer)

print(f"Jeder Gast bezahlt {bill_per_customer} €.\nDiese Betrag setzt sich aus dem Anteil von {bill_slice} € und "
      f"dem Trinkgeld in Höhe von {tip_per_customer_in_eur} € zusammen.\nInsgesamt erhält der Service ein Trinkgeld in "
      f"Höhe von {tip_total} €")
