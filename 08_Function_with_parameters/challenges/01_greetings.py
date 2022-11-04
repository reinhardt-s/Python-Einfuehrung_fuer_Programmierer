# Schriebe eine Funktion, die mich mit einem print-Statement begrüßt
def greet_me():
    print("Hello there.")


greet_me()


def greet_me_with_name(name):
    print(f"{name}. You are a bold one. Kill him!")


greet_me_with_name("General Kenobi")


def brag(route, time):
    print(f"It’s the ship that made the {route} in less than {time} parsecs.")


# Positional Argument
brag("Kessel-Run", 12)

# Keyword Arguments
brag(time=12, route="Kessel Run")
