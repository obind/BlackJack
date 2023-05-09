import random

def deal_card():
    """Gibt eine zufällige Karte aus."""
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♠', '♡', '♢', '♣']
    rank = random.choice(ranks)
    suit = random.choice(suits)
    return (rank, suit)

def card_value(card):
    """Gibt den Wert einer Karte zurück."""
    rank, _ = card
    if rank == 'A':
        return 11
    elif rank in ['K', 'Q', 'J']:
        return 10
    else:
        return int(rank)

def calculate_score(cards):
    """Berechnet die Punktzahl basierend auf einer Liste von Karten."""
    score = sum(card_value(card) for card in cards)
    has_ace = any(card[0] == 'A' for card in cards)
    if score > 21 and has_ace:
        score -= 10
    return score

def format_card(card):
    rank, suit = card
    return f"{rank}{suit}"

def display_cards(cards, hide_first=False):
    if hide_first:
        return f"[X], {', '.join(format_card(card) for card in cards[1:])}"
    else:
        return ', '.join(format_card(card) for card in cards)

def compare_scores(user_score, computer_score):
    if user_score == computer_score:
        return "Unentschieden!"
    elif computer_score == 21:
        return "Verloren, der Computer hat einen Blackjack!"
    elif user_score == 21:
        return "Gewonnen, Blackjack!"
    elif user_score > 21:
        return "Verloren, über 21 Punkte!"
    elif computer_score > 21:
        return "Gewonnen, Computer hat über 21 Punkte!"
    elif user_score > computer_score:
        return "Gewonnen!"
    else:
        return "Verloren!"

def blackjack_game():
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Deine Karten: {display_cards(user_cards)}, aktuelle Punktzahl: {user_score}")
        print(f"Computer erste Karte: {display_cards(computer_cards, hide_first=True)}")

        if user_score == 21 or computer_score == 21 or user_score > 21:
            game_over = True
        else:
            user_continue = input("Möchten Sie eine weitere Karte ziehen? 'j' für Ja, 'n' für Nein: ")
            if user_continue.lower() == 'j':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 21 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Dein endgültiges Blatt: {display_cards(user_cards)}, endgültige Punktzahl: {user_score}")
    print(f"Computer endgültiges Blatt: {display_cards(computer_cards)}, endgültige Punktzahl: {computer_score}")
    print(compare_scores(user_score, computer_score))

if __name__ == "__main__":
    blackjack_game()

