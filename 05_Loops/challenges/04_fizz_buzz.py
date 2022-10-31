# Schreibe eine App welche das Gruppenwortspiel Fizz Buzz, bis zur Zahl 100 durchspielt:
# https://de.wikipedia.org/wiki/Fizz_buzz
# Die App gibt Fizz aus, wenn die Zahl durch drei teilbar ist oder Buzz, wenn sie durch fünf teilbar ist.
# Ist die Zahl zur fünf und drei teilbar, gibt die App Fizz Buzz aus. Ist die Zahl weder durch fünf, noch durch
# drei teilbar, gibt die App die Zahl selbst aus.
# Gib zuletzt aus, wie viel Fizz, Buzz und Fizz Buzz gefunden wurden

# Dein Code nach dieser Zeile
count_fizz = 0
count_buzz = 0
count_fizz_buzz = 0
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
        count_fizz_buzz += 1
    elif number % 3 == 0:
        print("Fizz")
        count_fizz += 1
    elif number % 5 == 0:
        print("Buzz")
        count_buzz += 1
    else:
        print(number)

print(f"Fizz: {count_fizz}\nBuzz: {count_buzz}\nFizz Buzz: {count_fizz_buzz}")
