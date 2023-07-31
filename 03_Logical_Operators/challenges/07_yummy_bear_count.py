# Werkstudent Hannes wurde in der QA damit beauftragt, aufzuschreiben, wie viele Yummy-Bears, je Farbe in einer Tüte
# sind. Hannes hat seine Aufgabe nicht richtig verstanden und hat hintereinander weg, Buchstaben aufgeschrieben, welche
# die Farbe eines Yummy-Bears repräsentieren. Er hat dabei keine
# Rücksicht darauf genommen, ob er nun einen Großbuchstaben verwendet oder nicht.
# w/W = weiß
# o/O = orange
# y/Y = Gelb
# r/R = Rot
# p/P = Purpur
# g/G = Grün
# Schreibe ein Programm, das die Anzahl an verschiedenen Yummy-Bears zählt und diese ausgibt.
# Das Programm soll dann, nach den folgenden Kriterien entscheiden, ob die Tüte den Qualitätsansprüchen genügt und gibt
# Entweder "Bestanden" oder ein Kriterium aus, an dem es gescheitert ist.
#
# Es müssen mehr weiße als rote Yummies in der Tüte sein.
# Es müssen weniger gelbe als orange Yummies in der Tüte sein.
# Es müssen mindestens 84 und maximal 85 Yummies in der Tüte sein.
# Es müssen je Farbe mindestens 10 Yummies in der Tüte sein.
# Rote und purpurenen Yummies dürfen zusammen maximal 30 ergeben.
# Wenn mehr purpurene als gelbe Yummies in der Tüte sind müssen mehr weiße als rote in der Tüte sein.
#

bag = 'wOpoRYGWoyworoyOoWyoprorrWYRYrgOgRowwrWgPpypwrPwpwypwRywPYPRrwpYGwpWGwYGgwWOorgpyorPY'

# Dein Code unter dieser Zeile

bag = bag.lower()
w = bag.count("w")
o = bag.count("o")
y = bag.count("y")
r = bag.count("r")
p = bag.count("p")
g = bag.count("g")
count = len(bag)

print(f"Weiß: {w}\nOrange: {o}\nGelb: {y}\nRot: {r}\nPurpur: {p}\nGelb: {g}\nGesamt: {count}")

if w < 10 or o < 10 or y < 10 or r < 10 or p < 10 or g < 10:
    print("Von mindestens einer Farbe sind weniger als 10 Yummie-Bears in der Tüte")
elif r+p > 30:
    print("Rote + purpurene Yummie-Bears sind mehr als 30")
elif r > w:
    print("Mehr rote als weiße Yummie-Bears in der Tüte")
elif g > o:
    print("Mehr gelbe als orangene Yummie-Bears in der Tüte")
elif p > g and not w > r:
    print("Es sind mehr purpurene als gelbe Yummies in der Tüte aber nicht mehr gelbe als rote")
elif count != 85 and count != 84:
    print("Die Anzahl Yummie-Bears ist entweder kleiner als 84 oder größer als 85")
else:
    print("Bestanden")

