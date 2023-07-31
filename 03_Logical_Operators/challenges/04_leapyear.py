# Schreibe ein Programm welches prüft, ob ein Jahr ein Schaltjahr ist
# Die gregorianische Schalttagsregelung besteht aus folgenden drei einzelnen Regeln:
# 1. Die durch 4 ganzzahlig teilbaren Jahre sind, abgesehen von den folgenden Ausnahmen, Schaltjahre.
# 2. Säkularjahre, also die Jahre, die ein Jahrhundert abschließen (z. B. 1800, 1900, 2100 und 2200),
#    sind, abgesehen von der folgenden Ausnahme, keine Schaltjahre.
# 3. Die durch 400 ganzzahlig teilbaren Säkularjahre, zum Beispiel das Jahr 2000, sind jedoch Schaltjahre.
# Quelle: https://de.wikipedia.org/wiki/Schaltjahr


year = int(input("Welches Jahr möchtest du prüfen?\n"))
# Dein Code nach dieser Zeile

is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(f"Das Jahr {year} ist {'ein' if is_leap_year else 'kein'} Schaltjahr")

# is_div_by_four = year % 4 == 0
# is_div_by_hundred = year % 100 == 0
# is_div_by_400 = year % 400 == 0
# 
# is_leap_year = False
# answer = "kein"
# 
# 
# if is_div_by_four:
#     if is_div_by_hundred:
#         if is_div_by_400:
#             is_leap_year = True
#     else:
#         is_leap_year = True
# 
# if is_leap_year:
#     answer = "ein"
# 
# print(f"Das Jahr {year} ist {answer} Schaltjahr")
