#Контроль карт, які вже були використані в грі
used_cards = {
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 0,
    "J": 0,   # Валет (J)
    "Q": 0,   # Дама (Q)
    "K": 0,   # Король (K)
    "A": 0    # Туз (A)
}

def used_cards_counter(*cards):
    for card in cards:
        cards_upper = card.upper()
        if cards_upper in used_cards:
            used_cards[cards_upper] += 1
    return used_cards

