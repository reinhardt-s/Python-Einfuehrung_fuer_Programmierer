# wir importieren von Turtle eine Schildkröte mit Stift!
#import turtle

# Turtle-Objekt leonardo wurde von turtle.Turtle() erstellt
#leonardo = turtle.Turtle()

# zur kürzeren notation und um nicht alles von turtle zu importieren
from turtle import Turtle, Screen

leonardo = Turtle()
donatello = Turtle()
# zeigt, dass ein object erstellt wurde
print(leonardo)

## folgt erst nach exitonclick
# leonardo.shape("turtle")

# https://docs.python.org/3/library/turtle.html
# color ->
leonardo.color("blue")
donatello.forward(200)
leonardo.left(90)
leonardo.forward(150)

# zugriff auf attribute
# zugriff erfolgt über .
my_screen = Screen()
print(my_screen.canvheight)

# zugriff auf methoden
# zugriff erfolgt auch über punkt

#programm läuft bis gecklickt wird
my_screen.exitonclick()

