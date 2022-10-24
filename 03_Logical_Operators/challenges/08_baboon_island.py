# Schreibe ein Textadventure das sich an den Entscheidungsbaum aus der SVG-Datei orientiert.
# Du kannst die Texte austauschen, die Verzweigungen müssen jedoch bestehen bleiben
# Anforderungen:
# Eingaben von der Spieler*in werden in Kleinbuchstaben umgewandelt
# Lege eine Variable 'inventar' an. In dieser wird später ein String gespeichert, der angibt,
# welches Objekt die Spieler*in mitgenommen hat.
# Es kann vorkommen, dass die Spieler*in keine Entscheidung treffen muss und dennoch eine Verzweigung folgt.
# "~~~Dein Abenteuer endet hier.~~~" und "~~~Glückwunsch. Du hast das Spiel gemeistert.~~~" fangen immer in einer neuen
# Zeile an.
# Die eingaben der Spieler*in erfolgen immer in einer neuen Zeile

# Dein Coder nach dieser Zeile:

inventar = ""
print("~~~~Willkommen auf Baboon Island~~~~\n")
print("Irgendwo auf dieser Insel ist eine goldene Pavian-Statue. Finde Sie und überlebe.\n")
decision = input("Du hast am Strand angelegt. Du kannst entweder weiter am \"Strand\" laufen oder in den \"Dschungel\""
                 "\ngehen. Was tust du?\n").lower()
if decision == "dschungel":
    decision = input("Du kämpfst dich durch den dichten Dschungel, kommst aber kaum voran. Mit der Machete könntest "
                     "\ndu dir einen Weg frei schlagen. Nutzt du deine \"Machete\" oder gehst du so \"weiter\"?\n")\
                .lower()
    if decision == "machete":
        print("\nSchon beim ersten Schwung mit der Machete wird dir klar, dass du mit der Machete nicht umgehen kannst."
              "\nDu rutscht ab, schneidest ein dünnes Stück Holz ab, welches als fieser kleine Splitter nun in deiner "
              "\nHand steckt. Jede Bewegung mit der Hand tut nun voll weh.\n~~~Dein Abenteuer endet hier.~~~")
    else:  # weiter
        decision = input("Du kommst an einer Steintafel an auf der folgendes geschrieben steht: \"Womit jagen Paviane "
                         "Fische?\"\nDarunter sind zwei herausgehobene Bilder zu sehen. Ein \"Speer\" und \"Käscher\""
                         ".\nWorauf drückst du?\n").lower()
        if decision == "speer":
            inventar = "banane"
        else:  # käscher
            inventar = "auge"
        print("Nach dem du den halben Tag gesucht hast, kommst du an eine Stelle an der sich zwei Palmen überkreuzen. "
              "\nEine davon hat eine bananenförmige Vertiefung.")
        if inventar == "banane":
            print("Du legst die goldene Banane in die Vertiefung. Erst passiert eine Weile nichts, doch als du gerade "
                  "\ngehen willst, sagt die linke Palme: \"Danke!\". Zwischen den Palmen knarrt es. Der Boden beginnt "
                  "\netwas zu wackeln und es öffnet sich eine verborgene Bodenklappe genau zwischen den beiden Bäumen."
                  "\nDu schaust hinein und findest: Die goldene Pavianstatue."
                  "\n~~~Glückwunsch. Du hast das Spiel gemeistert.~~~")
        else:  # auge
            print("Du läufst zurück in den Dschungel und holst dutzende Bananen von verschiedenen Bäumen. Doch keine "
                  "\nwill so recht passen. Eine Gruppe Paviane, die gerade vom Fischen kommt, läuft auf dich zu. Sie "
                  "\nhalten dir einen empörten Vortrag über Lebensmittelverschwendung und Schädigung des Ökosystems. "
                  "\n~~~Dein Abenteuer endet hier.~~~")
else:
    decision = input("Du triffst auf eine Gruppe Paviane, die am Speerfischen sind. Du kannst dich \"vorstellen\" "
                     "\noder \"fliehen\". Was tust du?\n").lower()
    if decision == "fliehen":
        print("Du stolperst über eine zerbrochene Riesenmuschel und schneidest dir dabei den Fuß auf."
              "\n~~~Dein Abenteuer endet hier.~~~")
    else:  # vorstellen
        print("Du gehst zu den Pavianen, stellst dich vor und schüttelst ein paar Hände. Nach einer halben Stunde "
              "\nbist du sicher, dass du das Jobinterview gemeistert hast. Doch die Paviane haben nie zurückgerufen. "
              "\n~~~Dein Abenteuer endet hier.~~~")
