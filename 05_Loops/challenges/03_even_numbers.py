# Schreibe eine App, welche alle geraden Zahlen zwischen 1 und 100 (inkl.) aufaddiert

sum_even_numbers = 0
for even_number in range(2, 101, 2):
    sum_even_numbers += even_number
print(f"Die Summe ist {sum_even_numbers}")