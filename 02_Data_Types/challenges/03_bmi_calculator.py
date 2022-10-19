# Erstellen Sie ein Programm, welches den BMI berechnet
# Fragen Sie dazu zunächst die Größe und das Gewicht der Nutzer*in ab
# Berechnen Sie dann das Ergebnis und geben es als Integer aus:
# Ihr BMI beträgt 23

height = input("Wie groß bist du in m: ")
weight = input("Wie vie wiegst du in kg: ")

bmi = float(weight) / float(height)**2

print("Dein BMI beträgt: " + str(int(bmi)))
