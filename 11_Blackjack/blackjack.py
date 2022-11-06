import random

# Blackjack!
# Das Kartendeck hat eine unbegrenzte Größe
# Es gibt keine Joker
# Bube, Dame, König zählen 10
# Ass wird als 11 gezählt. Falls sich der Spieler überkaufen sollte und ein Ass in der Hand hält, wird
# dieses als 1 gezählt
# Du kannst ein Deck wie folgt definieren:
# * cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# Jede Karte in cards hat die gleiche Wahrscheinlichkeit gezogen zu werden
# Da das Deck unendlich ist, werden gezogene Karten nicht aus dem Deck entfernt
# Die Spieler*in verliert, bei Gleichstand mit 21, wenn sie sich überkauft und wenn der Computer näher an der 21
# ist (und sich dabei nicht überkauft hat,
# Die Spielerin gewinnt sofort bei, wenn Sie mit zwei Karten auf 21 kommt

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "Überkauft. Du verlierst"

    if user_score == computer_score:
        return "Gleichstand"
    elif computer_score == 0:
        return "Der Computer hat Blackjack! Du verlierst"
    elif user_score == 0:
        return "Du hast Blackjack und gewinnst"
    elif user_score > 21:
        return "Du hast dich überkauft und verlierst"
    elif computer_score > 21:
        return "Der Computer hat sich überkauft und du verlierst"
    elif user_score > computer_score:
        return "Du gewinnst"
    else:
        return "Du verlierst"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Deine Hand: {user_cards}, Deine Punkte: {user_score}")
        print(f"Erste Karte des Computers: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Weitere (K)arte oder lieber (n)icht?")
            if user_should_deal.lower() == "k":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Deine Hand: {user_cards}, Dein finaler Punktestand: {user_score}")
    print(f"Hand des Computers: {computer_cards}, Computers finaler Punktestand: {computer_score}")
    print(compare(user_score, computer_score))


while input("Lust auf eine Runde Blackjack? J/N\n").lower() == "j":
    play_game()
