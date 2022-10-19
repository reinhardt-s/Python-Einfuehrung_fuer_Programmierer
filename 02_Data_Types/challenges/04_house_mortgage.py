# Schreiben Sie ein Programm, welche die restliche Kreditlaufzeit berechnet und in Jahren, Monaten, wochen und Tagen
# ausgibt

years_total = 25
payed_years = input("Wie viele Jahre hast du schon abbezahlt: ")
# Schreiben Sie Ihren Code unter dieser Zeile

remaining_years = years_total - int(payed_years)
remaining_months = remaining_years * 12
remaining_weeks = remaining_years * 52
remaining_days = remaining_weeks * 7

print(f"Du muss noch {remaining_years} Jahre oder {remaining_months} Monate oder {remaining_weeks} Wochen oder {remaining_days} Tage den Kredit "
      f"abbezahlen")
